import re

with open('best-appendix-surgery-in-delhi-india.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'sketch_appendix_surgeon_1785927623986.png': 'sketch_appendix_surgeon_simple_1785928370631.png',
    'sketch_appendix_overview_1785927635175.png': 'sketch_appendix_overview_simple_1785929047139.png',
    'sketch_appendix_symptoms_1785927647316.png': 'sketch_appendix_symptoms_simple_1785929056487.png',
    'sketch_appendix_laparoscopic_1785927658976.png': 'sketch_appendix_laparoscopic_simple_1785929066310.png',
    'sketch_appendix_danger_1785927669702.png': 'sketch_appendix_danger_simple_1785929075570.png',
    'sketch_appendix_recovery_1785927682071.png': 'sketch_appendix_recovery_simple_1785929085614.png'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('best-appendix-surgery-in-delhi-india.html', 'w', encoding='utf-8') as f:
    f.write(content)
