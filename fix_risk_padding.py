import re

files = ['hernia-surgery-in-delhi.html', 'best-gallbladder-surgery-in-delhi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the mobile padding fixes block and add .risk-card
    if '.risk-card {' not in html.split('/* --- MOBILE PADDING FIXES --- */')[-1]:
        html = html.replace('/* --- MOBILE PADDING FIXES --- */', '/* --- MOBILE PADDING FIXES --- */\n      .risk-card { padding: 1.5rem 1.25rem !important; }\n      .four-f-item { padding: 1rem !important; }')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Risk card padding fixed.")
