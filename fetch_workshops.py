import urllib.request
from bs4 import BeautifulSoup

url = "https://www.atulpeters.com/workshop-conferences"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    for script in soup(["script", "style", "nav", "header", "footer"]):
        script.extract()
        
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    with open('workshop_dump.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("Successfully dumped workshop content to workshop_dump.txt")
except Exception as e:
    print("Error:", e)
