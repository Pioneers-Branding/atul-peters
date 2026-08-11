import re

with open('best-gallbladder-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    gb_html = f.read()

with open('hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    hr_html = f.read()


# 1. Update Hero CSS
# Extract gb-hero css
gb_hero_css = re.search(r'(\.gb-hero \{.*?\})', gb_html, re.DOTALL).group(1)
gb_hero_grad = re.search(r'(@keyframes hero-grad-shift \{.*?\})', gb_html, re.DOTALL).group(1)
gb_hero_blob = re.search(r'(\.gb-hero-blob \{.*?\})', gb_html, re.DOTALL).group(1)
gb_blob_float = re.search(r'(@keyframes blob-float \{.*?\})', gb_html, re.DOTALL).group(1)
gb_stat_pill = re.search(r'(\.gb-stat-pill \{.*?\})', gb_html, re.DOTALL).group(1)

# Extract sketch watermark CSS
sketch_css = re.search(r'(/\* ==========================================================================\s*CREATIVE BACKGROUND TEXTURE.*?</style>)', gb_html, re.DOTALL).group(1)
sketch_css = sketch_css.replace('.gb-', '.hr-')
# Remove </style> from sketch_css so we can just append it before </style> in hr_html
sketch_css = sketch_css.replace('</style>', '')

# We will replace the corresponding hr- classes in hr_html
hr_html = re.sub(r'\.hr-hero \{.*?\}', gb_hero_css.replace('.gb-', '.hr-'), hr_html, flags=re.DOTALL)
hr_html = re.sub(r'\.hr-hero-blob \{.*?\}', gb_hero_blob.replace('.gb-', '.hr-') + '\n\n    ' + gb_hero_grad + '\n\n    ' + gb_blob_float, hr_html, flags=re.DOTALL)
hr_html = re.sub(r'\.hr-stat-pill \{.*?\}', gb_stat_pill.replace('.gb-', '.hr-'), hr_html, flags=re.DOTALL)

# Append sketch css to the end of <style>
hr_html = hr_html.replace('  </style>', sketch_css + '\n  </style>')

# 2. Add "About Dr. Peters" section
about_section_match = re.search(r'(<section class="about-section section" id="about".*?</section>)', gb_html, re.DOTALL)
if about_section_match:
    about_section = about_section_match.group(1)
    hr_html = hr_html.replace('  <section class="hr-section hr-section--alt" id="recovery">', about_section + '\n\n  <section class="hr-section hr-section--alt" id="recovery">')

# 3. Add sketch watermarks to hernia sections
hero_watermark = '''
  <section class="hr-hero" style="position: relative; overflow: hidden;">
    <div class="hr-sketch-watermark" style="background-image: url('assets/img/sketch_hernia_surgeon_1785910965814.png'); width: 500px; height: 500px; top: 15%; left: -5%; transform: rotate(3deg) scaleX(-1);">
    </div>
'''
hr_html = hr_html.replace('  <section class="hr-hero">', hero_watermark)

overview_watermark = '''  <section class="hr-section" id="overview">
    <div class="hr-sketch-watermark"
      style="background-image: url('assets/img/sketch_hernia_defect_1785910910586.png'); width: 450px; height: 450px; top: 0%; right: 5%; transform: rotate(-5deg);">
    </div>'''
hr_html = hr_html.replace('  <section class="hr-section" id="overview">', overview_watermark)

types_watermark = '''  <section class="hr-section hr-section--alt" id="types">
    <div class="hr-sketch-watermark"
      style="background-image: url('assets/img/sketch_hernia_types_1785910928121.png'); width: 450px; height: 450px; top: 10%; left: -5%; transform: rotate(5deg);">
    </div>'''
hr_html = hr_html.replace('  <section class="hr-section hr-section--alt" id="types">', types_watermark)

tech_watermark = '''  <section class="hr-section" id="techniques" style="background-color: #f0f7ff; position: relative; overflow: hidden;">
    <div class="hr-sketch-watermark"
      style="background-image: url('assets/img/sketch_hernia_mesh_placement_1785910946322.png'); width: 500px; height: 500px; top: 15%; right: -5%; transform: rotate(-3deg);">
    </div>'''
hr_html = hr_html.replace('  <section class="hr-section" id="techniques">', tech_watermark)

recovery_watermark = '''  <section class="hr-section hr-section--alt" id="recovery" style="position: relative; overflow: hidden;">
    <div class="hr-sketch-watermark"
      style="background-image: url('assets/img/sketch_patient_walking_1785910955832.png'); width: 450px; height: 450px; top: 5%; right: 0%; transform: rotate(2deg);">
    </div>'''
hr_html = hr_html.replace('  <section class="hr-section hr-section--alt" id="recovery">', recovery_watermark)


with open('hernia-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(hr_html)

print("Done")
