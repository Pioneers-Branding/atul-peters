import os

files = [
    r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html',
    r'e:\atul-peters\atul-peters\best-gallbladder-surgery-in-delhi.html'
]

replacements = {
    'â€¢': '•',
    'â€“': '–',
    'â€”': '—',
    'â€™': '’',
    'â€œ': '“',
    'â€': '”',
    'â€"': '”', # sometimes quotes are weird
    'Â ': ' ', # nbsp
    'Â': '', # stray A-circumflex
    '?"': '–', # another common corruption for en-dash
    '+': '+',
    '': '-'
}

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for bad, good in replacements.items():
            content = content.replace(bad, good)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed encoding in {os.path.basename(filepath)}")
