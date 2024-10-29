import requests
import urllib

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()                    
    
    def get(self, endpoint: str, *args, **kwargs):
        return self.session.get(url=self.get_url(self.base_url, endpoint),
                                *args, **kwargs)
        
    @staticmethod        
    def get_url(base_url, endpoint) -> str:
        return urllib.parse.urljoin(base_url, endpoint)