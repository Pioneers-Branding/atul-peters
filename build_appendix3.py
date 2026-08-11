import re

with open('best-appendix-surgery-in-delhi-india.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'protocol in laparoscopic hernia reconstruction': 'protocol in laparoscopic appendix removal',
    'Ignoring a hernia': 'Ignoring an inflamed appendix',
    'Hernia Overview': 'Appendix Overview',
    'Understanding Hernias &amp; Warning Signs': 'Understanding Appendicitis &amp; Warning Signs',
    '4K laparoscopic and robotic hernia reconstruction surgery': '4K laparoscopic appendix removal surgery',
    'Hernias can occur in various parts of': 'Appendicitis is a medical emergency that',
    '</i> Hernia': '</i> Appendix',
    'alt="Laparoscopic Hernia Surgery Environment"': 'alt="Laparoscopic Appendix Surgery Environment"',
    'inflammation (Incarcerated Hernia).': 'inflammation and rupture.',
    'keyhole hernia reconstruction': 'keyhole appendix removal',
}

for old, new in replacements.items():
    content = re.sub(re.escape(old), new, content, flags=re.IGNORECASE)

# Special case for "Other Surgeries/laparoscopic-hernia.html" - we want to keep the URL as is since it points to a real page! But wait, if it's the breadcrumb text, we should keep it if it means Hernia.
# Wait, let's just make sure we don't have any loose 'hernia' text in user-facing content.

matches = set(re.findall(r'.{0,30}hernia.{0,30}', content, re.IGNORECASE))
print(f"Remaining hernia matches: {len(matches)}")
for m in matches:
    print(repr(m))

with open('best-appendix-surgery-in-delhi-india.html', 'w', encoding='utf-8') as f:
    f.write(content)
