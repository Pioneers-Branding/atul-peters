import re

header_path = r'e:\atul-peters\atul-peters\partials\header.js'
with open(header_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_style = '''<style>
/* --- MOBILE HEADER ALIGNMENT FIXES --- */
@media (max-width: 991px) {
  /* Hide the stray vertical divider since the badge is hidden */
  .top-bar-divider { display: none !important; }
  
  /* Ensure top bar looks right and phone numbers don't wrap weirdly */
  .top-bar-left { flex-wrap: nowrap !important; gap: 10px !important; justify-content: center !important; }
  
  /* FIX THE MYSTERY WHITE GAP: The mobile menu was translating UP by -110% 
     and its bottom edge was peeking out between the top-bar and navbar! 
     We force it to be completely invisible and pushed far away when closed. */
  .nav-menu:not(.open) {
    opacity: 0 !important;
    pointer-events: none !important;
    visibility: hidden !important;
    transform: translateY(-200%) !important;
  }

  /* Prevent logo from being cut off if it's too tall */
  .nav-logo img {
    max-height: 45px !important;
    width: auto !important;
    object-fit: contain !important;
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
print("Header CSS replaced with surgical fix.")
