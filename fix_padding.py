import re

files = ['hernia-surgery-in-delhi.html', 'best-gallbladder-surgery-in-delhi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Reduce padding for .diag-box on mobile
    if '@media (max-width: 768px)' not in html.split('.diag-box {')[1].split('}')[1]: # Check if a media query for diag-box exists right after
        # It probably doesn't.
        pass
    # We can just add a global @media block at the end of the style tag to safely override all padding issues.
    
    mobile_fixes = '''
    /* --- MOBILE PADDING FIXES --- */
    @media (max-width: 768px) {
      .diag-box {
        padding: 2rem 1.25rem !important;
      }
      .tech-card {
        padding: 1.75rem 1.25rem !important;
      }
      .finance-card {
        padding: 1.75rem 1.25rem !important;
        border-radius: 1.5rem !important;
      }
      .creative-info-section {
        padding: 2rem 1.25rem !important;
      }
      .gb-section {
        padding: 2.5rem 0 !important;
      }
      .gb-journey-card {
        padding: 1.5rem 1.25rem !important;
      }
      .diet-modern-card {
        padding: 1.75rem 1.25rem !important;
      }
      .gb-hotspot-card {
        padding: 1.5rem 1.25rem !important;
      }
    }
    '''
    
    if '/* --- MOBILE PADDING FIXES --- */' not in html:
        html = html.replace('</style>', mobile_fixes + '\n  </style>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Padding fixes applied.")
