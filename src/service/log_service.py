from tabulate import tabulate

headers = ["Name", "Package", "Criticality", "Manager", "Date", "URL"]

def display_data(data):    
    print(tabulate(data,
                   headers=headers,
                   tablefmt="grid",
                   stralign="left",
                   maxcolwidths=[20, 30, 10, 10, 15, 70]
                   ))

@staticmethod    
def display_tip():
    print("[+] Snyk Vulnerability DB Search Tool [+]\n"              
              "How to use:\n"
              "python main.py <term-to-search>") 