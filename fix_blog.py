import re

with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix common paths to add ../ prefix
content = re.sub(r'(href|src)="styles\.css"', r'\1="../styles.css"', content)
content = re.sub(r'(href|src)="(partials/.*?)"', r'\1="../\2"', content)
content = re.sub(r'(href|src)="(assets/.*?)"', r'\1="../\2"', content)
content = re.sub(r'(href|src)="(index\.html)"', r'\1="../\2"', content)
content = re.sub(r'(href)="(news\.html)"', r'\1="../\2"', content)

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated blog/index.html paths.')
