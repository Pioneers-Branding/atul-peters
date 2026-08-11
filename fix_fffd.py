import os
import re

files = [
    r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html',
    r'e:\atul-peters\atul-peters\best-gallbladder-surgery-in-delhi.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace U+FFFD with '-' for now, or print them
    if '\uFFFD' in content:
        print(f"Found U+FFFD in {filepath}")
        content = content.replace('\uFFFD', '-')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
