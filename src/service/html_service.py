from src.config.strings import END, CRITICAL, HIGH, MEDIUM, LOW, REFRESHING
from bs4 import BeautifulSoup
from src.config.env import ENV
from src.service.http_service import HttpClient
from src.service import security_service as security

def its_over(html_data):    
    return (END in html_data or REFRESHING in html_data)

def build_items(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
            
    td_content = []
    vulnerabilities = []
    
    # Find all <td> tags
    td_tags = soup.find_all('td')
    
    # temporary data
    href_content = ''
    severity = ''
    
    for td in td_tags:
        try:
            # Get text content of the <td>
            content = td.get_text(strip=True)
            td_content.append(content)
        
            # Find all <a> tags inside td
            a_tag = td.find('a')
            
            # Find all <abbr> tags inside td
            abbr_tag = td.find('abbr') 
            
            # Get the severity atribute inside <abbr> tag
            if(abbr_tag != None and 'title' in abbr_tag.attrs):
                abbr_title = abbr_tag['title']
                severity = get_severity(abbr_title)
                
            # Get the first href atribute that is the vulnerability details endpoint
            if (a_tag != None and 'href' in a_tag.attrs and href_content == ''):
                href_content = a_tag['href']                        
            
            # build Vulnerability after each 4 <td> data fragment            
            if(len(td_content) == 4):
                                        
                security.check_path(href_content)     
                security.check_date(td_content[3]) 
                            
                url = build_url(security.sanitize(href_content))                  
                name = security.sanitize(td_content[0])  
                package = security.sanitize(td_content[1])
                manager = security.sanitize(td_content[2])
                date = security.sanitize(td_content[3])                        
                                                                    
                vul = [
                        str(name[1:]), # we split the 1st char of the name, that contains the indicator of severity
                        str(package),
                        str(severity),      
                        str(manager),
                        str(date), 
                        str(url)
                ]                        
                
                vulnerabilities.append(vul)            
                #clear temporary data
                severity = ''
                href_content = ''                
                td_content.clear()
                
        except Exception:
            print(f"Error while parsing <td> tags for {td}")
                                                                           
    return vulnerabilities

def get_severity(title):
            
    if(CRITICAL in title): return CRITICAL
    if(HIGH in title): return HIGH
    if(MEDIUM in title): return MEDIUM
    if(LOW in title): return LOW
    
    print(f"Severity not learned {title}")
    
    
def build_url(href):
    return HttpClient.get_url(ENV.SNYK_HOST, href)