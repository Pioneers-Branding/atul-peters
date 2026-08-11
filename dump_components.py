import re

with open(r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find cvs-suite
cvs_match = re.search(r'<div class="cvs-suite">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if cvs_match:
    with open('cvs_suite.txt', 'w', encoding='utf-8') as f:
        f.write(cvs_match.group(0))

# find tech-grid
tech_match = re.search(r'<div class="tech-grid">.*?</div>\s*</div>', html, re.DOTALL)
if tech_match:
    with open('tech_grid.txt', 'w', encoding='utf-8') as f:
        f.write(tech_match.group(0))

# find timeline
timeline_match = re.search(r'<div class="journey-interactive">.*?</section>', html, re.DOTALL)
if timeline_match:
    with open('timeline.txt', 'w', encoding='utf-8') as f:
        f.write(timeline_match.group(0))
