import re

with open(r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id=\"([^\"]+)\"[^>]*>', html)
print("Sections found:", sections)
