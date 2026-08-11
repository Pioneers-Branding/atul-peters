import re

header_path = r'e:\atul-peters\atul-peters\partials\header.js'
with open(header_path, 'r', encoding='utf-8') as f:
    html = f.read()

fix_style = '''
<style>
/* --- MOBILE HEADER ALIGNMENT FIXES --- */
@media (max-width: 991px) {
  .top-bar-divider { display: none !important; }
  .top-bar { margin-bottom: 0 !important; padding-bottom: 0.5rem !important; }
  .navbar { margin-top: 0 !important; top: 0 !important; }
  .nav-logo { display: flex !important; align-items: center !important; height: 100% !important; overflow: visible !important; }
  .nav-logo img { max-height: 45px !important; object-fit: contain !important; margin: 0 !important; padding: 0 !important; position: relative !important; top: 0 !important; }
}
</style>
'''

if '/* --- MOBILE HEADER ALIGNMENT FIXES --- */' not in html:
    html = html.replace('</nav>', fix_style + '</nav>')
    with open(header_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Header fixed.")
else:
    print("Fix already exists.")
