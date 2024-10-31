import html
from datetime import datetime
from urllib.parse import urlparse
from src.service import log_service
import re
import sys

def check_length(data):
    max_length = 1000
    
    if(len(data) > max_length):
        raise ValueError("Input is too large.")

def sanitize(data):
    
    bad_chars = "*#@!"
    
    # HTML escaping to prevent XSS if data would be now or in future used for other applications
    safe_data = html.escape(data)
    
    # check for incomon input data size
    check_length(safe_data)
    
    # replace some bad chars
    for char in bad_chars:
        safe_data = safe_data.replace(char, "")
    
    return safe_data
                
def check_date(date):
    try:
        # -> day-month-year
        datetime.strptime(date, "%d %b %Y")
        return True
    except ValueError:
        raise ValueError(f"Date informed is not Well Formed: {date}")
                
def check_path(path):    
    parsed_url = urlparse(path)
        
    if not parsed_url.scheme and not parsed_url.netloc and parsed_url.path:
        return True
    else:
        raise ValueError(f"Invalid URL path: '{path}'")
    
def check_args(args):
    term_pattern = r"^[a-zA-Z0-9-]+$" 
    lenght = len(args)      
        
    if (lenght == 2 and re.fullmatch(term_pattern, args[1])):
        return
    else:
        log_service.display_tip()
        sys.exit(1)