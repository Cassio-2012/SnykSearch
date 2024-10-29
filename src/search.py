from src.service.snyk_service import SnykService
import src.service.html_service as html
from src.service import log_service
from src.service import security_service as security
import time
import secrets

class SnykSearch:
    def __init__(self, argv):
        self.argv = argv
        self.snyk = SnykService  
        
    def run(self):        
        print("Performin search ... ")
        sanitized_arg = security.sanitize(self.argv[1])          
        self.search_with_term(sanitized_arg)                                                       
                                             
    def search_with_term(self, term):
        
        vulnerabilities = []        
        page = 1
        
        while True:                    
            http_response = self.snyk.search_with_term(term, page)     
                   
            if(html.its_over(http_response)):                
                break              
            items = html.build_items(http_response)
            vulnerabilities.extend(items)                                              
            page +=1 
            
            self.delay()            
        
        if(len(vulnerabilities) > 0):
            log_service.display_data(vulnerabilities)
        else:
            print("[-] No vulnerabilities found")
                        
    def delay(self): 
           
        delay_time = secrets.choice([i / 10 for i in range(10, 41)])  # Random float between 1.0 and 4.0
        time.sleep(delay_time)                
