import os

files = [
    r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html',
    r'e:\atul-peters\atul-peters\best-gallbladder-surgery-in-delhi.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'â' in content:
        print(f"Found corrupted chars in {os.path.basename(filepath)}")
        import re
        matches = set(re.findall(r'â.{1,3}', content))
        for m in matches:
            print(repr(m))
