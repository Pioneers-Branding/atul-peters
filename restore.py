import os

files = [
    r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html',
    r'e:\atul-peters\atul-peters\best-gallbladder-surgery-in-delhi.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if '-<-!-D-O-C-T-Y-P-E-' in content:
        print(f"Restoring {os.path.basename(filepath)}")
        # The replacement content.replace('', '-') inserts - at index 0, 2, 4
        # Original string len N becomes 2N+1
        original_content = content[1::2]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(original_content)
