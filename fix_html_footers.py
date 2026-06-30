import re
files = ['disclaimer.html', 'privacy-policy.html', 'weight-loss-surgery/faqs.html', 'weight-loss-surgery/intra-gastric-balloon.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine if we need '../'
    script_src = '../partials/footer.js' if 'weight-loss-surgery' in file else 'partials/footer.js'
    
    # Replace the fetch logic with the script tag (handling newlines inside the script tag)
    pattern = r'<div id=\"footer-placeholder\"></div>\s*<script>\s*fetch[\s\S]*?</script>'
    
    if re.search(pattern, content):
        content = re.sub(pattern, f'<!-- Global Footer -->\n  <script src="{script_src}"></script>', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')
    else:
        print(f'Pattern not found in {file}')
