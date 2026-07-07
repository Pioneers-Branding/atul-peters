import re
with open('partials/footer.js', 'r', encoding='utf-8') as f:
    content = f.read()

base_logic = '''var basePath = '';
if (window.location.pathname.indexOf('/weight-loss-surgery/') !== -1 || window.location.pathname.indexOf('/surgery-for-diabetes/') !== -1) {
  basePath = '../';
}

'''
if 'var basePath' not in content and 'let basePath' not in content:
    content = base_logic + content

# Replace href=\"somefile.html\" with href=\"${basePath}somefile.html\"
# We should avoid replacing already prefixed ones like href=\"${basePath}...\"
# Also avoid href=\"tel:...\", href=\"mailto:...\", href=\"http...\"
content = re.sub(r'href="(?!tel:|mailto:|http|\#|\$\{basePath\})([^"]+)"', r'href="${basePath}\1"', content)
content = re.sub(r'href=\'(?!tel:|mailto:|http|\#|\$\{basePath\})([^\']+)\'', r'href=\'${basePath}\1\'', content)

content = re.sub(r'src="(?!tel:|mailto:|http|data:|\#|\$\{basePath\})([^"]+)"', r'src="${basePath}\1"', content)
content = re.sub(r'src=\'(?!tel:|mailto:|http|data:|\#|\$\{basePath\})([^\']+)\'', r'src=\'${basePath}\1\'', content)

with open('partials/footer.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
