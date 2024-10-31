import sys
from src.search import SnykSearch
from src.service import security_service as security

def main(argv):
    security.check_args(argv)    
    app = SnykSearch(argv)        
        
    try:
        app.run()
    except Exception as e:
        print(f"An exception occurred: {e}")
        sys.exit(1)    
    
if __name__ == '__main__':
    main(sys.argv)            