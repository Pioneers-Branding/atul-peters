import re

with open(r'e:\atul-peters\atul-peters\robotic-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div class="gb-card-icon">\s*<i class="(.*?)"></i>\s*</div>\s*<h3>(.*?)</h3>'
replacement = r'<h3><i class="\1" style="color: var(--blue);"></i> \2</h3>'

new_html = re.sub(pattern, replacement, html)

with open(r'e:\atul-peters\atul-peters\robotic-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Restructured gb-card-icon')
