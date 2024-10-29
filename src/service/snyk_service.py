from src.config.env import ENV
from src.service.http_service import HttpClient

class SnykService:
    def __init__(self):
        self.client = HttpClient(ENV.SNYK_HOST)
        
    def search_with_term(self, term: str, page: int):
        
        try:            
            if(page == 1):            
                res = self.client.get(ENV.SNYK_PATH, params={ENV.SNYK_PARAM: term})                                                           
                return res.text
            else:
                res = self.client.get(f'{ENV.SNYK_PATH}/{page}', params={ENV.SNYK_PARAM: term})            
                return res.text
            
        except Exception as e:
            print(f"Error while searching [term]: {term}  -- {e}")
                
SnykService = SnykService()