import os
file_path = r'e:\atul-peters\atul-peters\weight-loss-surgery\mini-gastric-bypass.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '<img src="https://www.atulpeters.com/front/img/mini-gastric-img.png" alt="Mini Gastric Bypass Illustration">'
replacement = '<img src="https://www.atulpeters.com/front/img/mini-gastric-img.png" alt="Mini Gastric Bypass Illustration" style="object-fit: contain !important; height: auto;">'
text = text.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Edited MGB image styling')
