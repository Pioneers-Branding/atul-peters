import os

filepath = r'e:\atul-peters\atul-peters\best-gallbladder-surgery-in-delhi.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if 'ABOUT SECTION MOBILE HOTFIX' not in content:
    content = content.replace('</head>', '''<style>
/* ABOUT SECTION MOBILE HOTFIX - INJECTED */
@media (max-width: 991px) {
  .about-photo-stack {
    padding-left: 0 !important;
    padding-bottom: 2rem !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
  }
  .about-photo-bg {
    display: none !important; /* Hide the background block entirely on mobile to prevent overlapping */
  }
  .about-photo-frame {
    margin: 0 auto 15px auto !important;
    width: 100% !important;
    max-width: 400px !important;
    z-index: 2 !important;
  }
  .about-ribbon {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    width: 100% !important;
    max-width: 400px !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    margin: 0 auto !important;
    padding: 15px !important;
    z-index: 99 !important; /* Force to top */
    border-radius: 8px !important;
    background: var(--blue-deep) !important;
  }
  .about-ribbon::before {
    display: none !important;
  }
  .about-ribbon-divider {
    width: 1px !important;
    height: auto !important;
    background: rgba(255,255,255,0.2) !important;
    margin: 0 10px !important;
  }
  .about-ribbon-item {
    flex: 1 !important;
    align-items: center !important;
    text-align: center !important;
  }
}
</style>\n</head>''')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
