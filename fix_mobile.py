import re

files = ['hernia-surgery-in-delhi.html', 'best-gallbladder-surgery-in-delhi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the block @media (max-width: 768px) { .gb-sketch-watermark { ... } }
    pattern = r'@media \(max-width: 768px\) \{\s*\.gb-sketch-watermark \{.*?\}\s*\}'
    replacement = '''@media (max-width: 768px) {
      .gb-sketch-watermark {
        opacity: 0.4 !important;
        width: 160px !important;
        height: 160px !important;
        /* Allow inline styles to determine left/right corner placement creatively */
      }
    }'''
    
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Update complete")
