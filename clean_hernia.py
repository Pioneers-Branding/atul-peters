import re

with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Meta image
html = html.replace('assets/img/Hernia-Gallbladder-Surgery.webp', 'assets/img/doctor-portrait.webp')

# 3. Sketch watermark
html = re.sub(r'background-image: url\(\'assets/img/sketch_hernia_mesh_placement_1785910946322\.png\'\)', 'background-image: none', html)

# 4. Advanced techniques section text (which I missed)
html = html.replace('4K Laparoscopic eTEP &amp; Da Vinci Robotic Hernia Repair', 'Laparoscopic &amp; Robotic Gastric Bypass')
html = re.sub(r'hernia reconstruction utilizing state-of-the-art 4K Ultra HD vision systems and strict international safety', 'gastric bypass utilizing state-of-the-art 4K Ultra HD vision systems and robotic precision', html)
html = re.sub(r'<p class="tech-desc">For complex anatomical situations-such as massive incisional hernias or loss of domain.*?</div>', '<p class="tech-desc">The da Vinci Xi Robotic System provides 3D high-definition magnified optics and 360-degree articulation for unmatched precision during gastric bypass.</p></div>', html, flags=re.DOTALL)

# 5. Journey text (replace didn't work because of newlines perhaps)
html = re.sub(r'We combine Enhanced Recovery After Surgery \(ERAS\) pathways with compassionate hospital care to ensure your\s*hernia repair is swift, painless, and completely stress-free.', 'Most patients experience rapid weight loss in the first 6 months, followed by steady progress towards their goal over 18 to 24 months.', html, flags=re.DOTALL)

# 6. Diet text (replace didn't work because of newlines)
html = re.sub(r'After hernia reconstruction, most patients can resume their diet fairly quickly\. There are\s*generally no specific long-term dietary restrictions imposed by the surgery itself\.', 'The first step in your recovery is a structured clear liquid phase. Here are the essential Do\'s and Don\'ts.', html, flags=re.DOTALL)

# 7 & 8. FAQ header and extra FAQs
html = re.sub(r'Everything you need to know about undergoing safe, permanent hernia reconstruction with Dr\. Atul Peters in\s*Delhi', '9 of the most common questions about Roux-en-Y Gastric Bypass, answered by Dr. Atul Peters.', html, flags=re.DOTALL)

# I should probably just nuke any lingering FAQ list items about hernias. 
# Let's see if there's a `<div class="service-faq-grid">` left behind or something.
# The original script targeted `<div class="gb-faq-list">`. Let's just find "Can an abdominal or groin hernia heal" and remove it.
html = re.sub(r'<div class="gb-faq-item">.*?Can an abdominal or groin hernia heal without surgery.*?</div>\s*</div>', '', html, flags=re.DOTALL)

# 9. Appointment options
html = html.replace('<option selected="" value="laparoscopic-hernia">Laparoscopic Hernia Surgery</option>', '<option selected="" value="rygb">Roux-en-Y Gastric Bypass</option>')
html = html.replace('<option value="robotic-hernia">Robotic Hernia Surgery</option>', '<option value="sleeve">Sleeve Gastrectomy</option>')
html = html.replace('<option value="hernia">Not Sure Yet</option>', '<option value="other">Not Sure Yet</option>') # Just in case

# Fix the procedure header from the previous step
html = html.replace('<span class="gb-section-tag">Gold Standard Safety</span>', '<span class="gb-section-tag">The Procedure</span>')
html = html.replace('<h2 class="gb-section-title">The "Critical View of Safety" Technique</h2>', '<h2 class="gb-section-title">How Gastric Bypass Works</h2>')
html = re.sub(r'Dr\. Peters strictly adheres to the internationally mandated <strong>Critical View of Safety \(CVS\)</strong> protocol\. This ensures 100% anatomical clarity before any clipping or cutting, virtually eliminating the risk of accidental bile duct injury\.', 'A precise, minimally invasive surgery that creates a new pathway for digestion and absorption. Performed via 4K Laparoscopic or Robotic approach.', html, flags=re.DOTALL)


with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Final replacements done.")
