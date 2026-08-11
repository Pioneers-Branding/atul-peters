import re

with open('best-gallbladder-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    gb_html = f.read()

with open('hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    hr_html = f.read()

def get_block(text, start_str):
    start_idx = text.find(start_str)
    if start_idx == -1: return ''
    brace_count = 0
    in_block = False
    for i in range(start_idx, len(text)):
        if text[i] == '{':
            brace_count += 1
            in_block = True
        elif text[i] == '}':
            brace_count -= 1
            if in_block and brace_count == 0:
                return text[start_idx:i+1]
    return ''

gb_hero = get_block(gb_html, '.gb-hero {')
gb_hero_blob = get_block(gb_html, '.gb-hero-blob {')
gb_stat_pill = get_block(gb_html, '.gb-stat-pill {')
gb_hero_grad = get_block(gb_html, '@keyframes hero-grad-shift {')
gb_blob_float = get_block(gb_html, '@keyframes blob-float {')
sketch_watermark = get_block(gb_html, '.gb-sketch-watermark {')
body_pillar = get_block(gb_html, 'body.gb-pillar-page {')
body_pillar_before = get_block(gb_html, 'body.gb-pillar-page::before {')
body_pillar_after = get_block(gb_html, 'body.gb-pillar-page::after {')
doodle_float = get_block(gb_html, '@keyframes doodle-float {')

# Replace classes in hernia
hr_html = re.sub(r'\.hr-hero \{.*?\}', gb_hero.replace('.gb-', '.hr-'), hr_html, flags=re.DOTALL)
hr_html = re.sub(r'\.hr-hero-blob \{.*?\}', gb_hero_blob.replace('.gb-', '.hr-') + '\n\n    ' + gb_hero_grad + '\n\n    ' + gb_blob_float, hr_html, flags=re.DOTALL)
hr_html = re.sub(r'\.hr-stat-pill \{.*?\}', gb_stat_pill.replace('.gb-', '.hr-'), hr_html, flags=re.DOTALL)

# Append sketch css to the end of <style>
sketch_css = f'''
    /* ==========================================================================
       CREATIVE BACKGROUND TEXTURE & WATERMARKS
       ========================================================================== */
    {body_pillar.replace('.gb-', '.hr-')}
    {body_pillar_before.replace('.gb-', '.hr-')}
    {body_pillar_after.replace('.gb-', '.hr-')}
    
    {sketch_watermark.replace('.gb-', '.hr-')}
    
    {doodle_float}
'''
hr_html = hr_html.replace('  </style>', sketch_css + '\n  </style>')

# Add "About Dr. Peters" section
about_section_match = re.search(r'(<section class="about-section section" id="about".*?</section>)', gb_html, re.DOTALL)
if about_section_match:
    about_section = about_section_match.group(1)
    hr_html = hr_html.replace('  <section class="hr-section hr-section--alt" id="recovery">', about_section + '\n\n  <section class="hr-section hr-section--alt" id="recovery">')

# Add sketch watermarks to hernia sections
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

# Enhance .hr-card hover effect
hr_html = re.sub(r'(\.hr-card:hover \{.*?transform: translateY\()(-5px)(\).*?box-shadow: 0 )(15px 30px)( rgba\(0, 0, 0, 0.1\);.*?\})', r'\g<1>-10px\g<3>25px 50px\g<5>', hr_html, flags=re.DOTALL)

# Add glassmorphism to .hr-quick-nav
hr_html = re.sub(r'(\.hr-quick-nav \{.*?background: )(rgba\(255, 255, 255, 0.95\))(.*?\})', r'\g<1>rgba(255, 255, 255, 0.8)\n    backdrop-filter: blur(12px);\n    -webkit-backdrop-filter: blur(12px);\n    border-bottom: 1px solid rgba(255, 255, 255, 0.3);\g<3>', hr_html, flags=re.DOTALL)

# Apply better hover effect to .hr-type-card
hr_html = re.sub(r'(\.hr-type-card:hover \{.*?transform: translateY\()(-5px)(\).*?box-shadow: 0 )(15px 30px)( rgba\(0,0,0,0.1\);.*?\})', r'\g<1>-8px\g<3>20px 40px\g<5>', hr_html, flags=re.DOTALL)

with open('hernia-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(hr_html)

print("Done with safe CSS extraction.")
