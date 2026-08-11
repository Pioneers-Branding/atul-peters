import re

header_path = r'e:\atul-peters\atul-peters\partials\header.js'
with open(header_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_style = '''<style>
/* --- MOBILE HEADER ALIGNMENT FIXES --- */
@media (max-width: 991px) {
  .top-bar { 
    height: 40px !important; 
    overflow: hidden !important; 
    margin: 0 !important; 
    padding: 0 !important; 
    display: flex !important;
    align-items: center !important;
  }
  .top-bar-inner { 
    height: 100% !important; 
    margin: 0 !important; 
    padding: 0 15px !important; 
    width: 100% !important;
  }
  .top-bar-left { flex-wrap: nowrap !important; gap: 15px !important; }
  .top-bar-divider { display: none !important; }
  .top-bar-badge { display: none !important; }

  .navbar { 
    margin: 0 !important; 
    padding: 0 !important; 
    height: 65px !important; 
    top: 0 !important; 
    display: flex !important; 
    align-items: center !important; 
    border-top: none !important;
  }
  .nav-inner { 
    height: 100% !important; 
    margin: 0 !important; 
    align-items: center !important; 
    display: flex !important;
  }
  
  .nav-logo { 
    display: flex !important; 
    align-items: center !important; 
    height: 100% !important; 
  }
  .nav-logo img { 
    height: 45px !important; 
    max-height: 45px !important; 
    object-fit: contain !important; 
    margin: 0 !important; 
    padding: 0 !important;
  }
}
</style>'''

# Replace old injected block if it exists
pattern = r'<style>\s*/\* --- MOBILE HEADER ALIGNMENT FIXES --- \*/.*?</style>'
if re.search(pattern, html, flags=re.DOTALL):
    html = re.sub(pattern, new_style, html, flags=re.DOTALL)
else:
    html = html.replace('</nav>', new_style + '\n</nav>')

with open(header_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Header completely locked.")
