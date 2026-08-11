import re

with open('best-appendix-surgery-in-delhi-india.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    # Anatomy Section
    'Explore how hernias develop and the critical importance of placing the surgical mesh in the correct anatomical layer.': 'Explore how appendicitis develops and the critical importance of timely surgical removal before the organ ruptures.',
    'The Muscular Defect': 'The Inflamed Appendix',
    'The core issue is a physical hole in the strong fascial layer of your abdomen. Intestines or fat push through this gap, creating the visible bulge under your skin.': 'The core issue is a blockage in the appendix, leading to swelling, infection, and severe right-sided abdominal pain.',
    'Standard IPOM (Old Method)': 'Open Appendectomy (Old Method)',
    'Historically, mesh was placed directly inside the peritoneal cavity (IPOM), touching the bowels. This risked dangerous adhesions, chronic pain, and bowel fistulas.': 'Historically, a large 4-inch incision was made on the lower right abdomen, which required cutting through muscle, leading to severe pain and a long recovery.',
    'eTEP / TAR (Modern Standard)': 'Laparoscopic Surgery (Modern Standard)',
    'Dr. Peters utilizes the eTEP technique, placing the mesh outside the peritoneal cavity between muscle layers. This guarantees ZERO mesh-to-bowel contact and < 1% recurrence.': 'Dr. Peters utilizes laparoscopic techniques to safely extract the appendix without exposing the rest of the abdomen to infection. This guarantees rapid recovery and virtually zero recurrence.',
    
    # Advanced Surgical Options Section
    '4K Laparoscopic eTEP &amp; Da Vinci Robotic Hernia Repair': '4K Laparoscopic Appendectomy',
    'hernia reconstruction utilizing state-of-the-art 4K Ultra HD vision systems and strict international safety': 'appendix removal utilizing state-of-the-art 4K Ultra HD vision systems and strict international safety',
    '<h3 class="tech-title">4K HD Laparoscopic eTEP</h3>': '<h3 class="tech-title">4K HD Laparoscopic Surgery</h3>',
    'specialized micro-instruments are introduced. The defect is closed and a large mesh is placed extraperitoneally.': 'specialized micro-instruments are introduced. The inflamed appendix is carefully detached and safely extracted from the body.',
    '<h3 class="tech-title">Da Vinci Robotic TAR</h3>': '<h3 class="tech-title">Advanced Infection Control</h3>',
    'For complex anatomical situations—such as massive incisional hernias or loss of domain—the advanced Da Vinci Xi Robotic System provides 3D high-definition magnified optics and 360-degree wristed articulation.': 'For complex situations—such as a perforated appendix or severe abdominal infection—advanced laparoscopic optics provide 3D high-definition magnified vision to ensure thorough cleaning.',
    'Unparalleled precision for transversus abdominis release (TAR)': 'Unparalleled precision for removing severely inflamed tissue',

    # Extra Peritoneal Mesh / Safety Protocol Section
    'Extraperitoneal Mesh Placement': 'Safe Appendix Extraction Protocol',
    'To ensure <strong>100% patient safety</strong>, Dr. Atul Peters strictly places the prosthetic mesh in the retro-rectus or pre-peritoneal space, ensuring it never touches your delicate intestines.': 'To ensure <strong>100% patient safety</strong>, Dr. Atul Peters utilizes specialized endo-bags to extract the infected appendix, ensuring the infection never spills into your delicate abdominal cavity.',
    'Defect Closure Under Tension-Free State': 'Thorough Abdominal Lavage',
    'The muscular gap is primarily closed using strong sutures before any mesh is placed, restoring natural abdominal wall function and core strength.': 'If the appendix has ruptured, the abdominal cavity is thoroughly washed (lavage) with sterile fluids to remove all bacteria and prevent abscess formation.',
    'Sub-Lay Mesh Positioning': 'Secure Stump Closure',
    'A large, lightweight macroporous mesh is laid flat between the muscle layers, acting as a permanent reinforcement shield behind the defect.': 'The base of the appendix is securely sealed using advanced surgical clips or loops to prevent any leakage from the large intestine.',
    'Because the mesh is sealed behind the peritoneum, there is absolutely zero risk of it fusing with your intestines or causing chronic adhesions.': 'Because the infected tissue is completely removed, there is absolutely zero risk of appendicitis ever returning.',
    
    '<i class="fa-solid fa-triangle-exclamation"></i> Standard IPOM Mesh': '<i class="fa-solid fa-triangle-exclamation"></i> Delayed Surgery',
    'Placing mesh directly inside the abdominal cavity risks severe complications over time.': 'Delaying surgery risks severe, life-threatening complications.',
    'Mesh directly touching bowel loops': 'Appendix rupture and peritonitis',
    
    '<i class="fa-solid fa-shield-check"></i> Dr. Peters\' eTEP/TAR Protocol': '<i class="fa-solid fa-shield-check"></i> Dr. Peters\' Emergency Protocol',
    'The mesh is safely sandwiched within the muscle layers, restoring perfect anatomy.': 'The appendix is safely extracted through keyholes, restoring perfect health.',
    'Primary closure of the muscular defect': 'Complete removal of infected organ',
    'Mesh isolated from peritoneal cavity': 'Zero risk of recurrence',

    # About The Surgeon
    'complex abdominal wall reconstructions and hernia repairs': 'complex gastrointestinal and emergency surgeries including appendectomies',

    # Recovery
    'hernia repair is swift, painless, and completely stress-free.': 'appendix removal is swift, painless, and completely stress-free.',

    # Diet
    'Life After Hernia Surgery: What to Eat &amp; Activities': 'Life After Appendix Surgery: What to Eat &amp; Activities',
    'After hernia reconstruction, most patients can resume their diet fairly quickly.': 'After appendix removal, most patients can resume their diet fairly quickly.',

    # FAQ
    'Everything you need to know about undergoing safe, permanent hernia reconstruction with Dr. Atul Peters in Delhi NCR.': 'Everything you need to know about undergoing safe appendix removal with Dr. Atul Peters in Delhi NCR.',
    'Can an abdominal or groin hernia heal without surgery if I wear a hernia belt?': 'Can I take antibiotics instead of surgery?',
    
    # Form options
    '<option selected="" value="laparoscopic-hernia">Laparoscopic Hernia Surgery</option>': '<option selected="" value="laparoscopic-appendix">Laparoscopic Appendix Surgery</option>',
    '<option value="robotic-hernia">Robotic Hernia Surgery</option>': '<option value="emergency-appendix">Emergency Appendectomy</option>',
    '<option value="tar-reconstruction">Abdominal Wall Reconstruction</option>': '<option value="other">Other Query</option>'
}

# The long FAQ answer replacement
faq_old = '''No. A hernia is a mechanical physical hole or structural tear in your muscular fascia.
              Hernia belts, trusses, or abdominal binders merely apply external compression to temporarily keep the
              bulge pushed inside while you are wearing them; they do not close or repair the torn muscle layer. Over
              time, constant pressure from a tight belt can cause skin ulceration and make the underlying muscle edges
              more scarred and difficult to repair.'''
              
faq_new = '''While some mild cases of appendicitis have been treated with antibiotics alone in experimental settings, the international gold standard remains surgical removal. Antibiotic-only treatment has a high recurrence rate (the appendicitis comes back), and surgery is the only definitive, permanent cure to ensure it never returns.'''

# Remove whitespace to match easily
def normalize_space(s):
    return re.sub(r'\s+', ' ', s).strip()

content_norm = normalize_space(content)

for old, new in replacements.items():
    # Use simple replace first
    if old in content:
        content = content.replace(old, new)
    else:
        # Fallback to regex with flexible whitespace
        pattern = re.compile(re.escape(old).replace(r'\ ', r'\s+'), re.IGNORECASE)
        content = pattern.sub(new, content)

# Replace the FAQ manually with flexible whitespace matching
faq_old_norm = normalize_space(faq_old)
pattern = re.compile(re.escape(faq_old_norm).replace(r'\ ', r'\s+'), re.IGNORECASE)
content = pattern.sub(faq_new, content)

# Check for any remaining 'hernia' (case insensitive)
matches = set(re.findall(r'.{0,30}hernia.{0,30}', content, re.IGNORECASE))
print(f"Remaining hernia matches: {len(matches)}")
for m in matches:
    print(repr(m))

with open('best-appendix-surgery-in-delhi-india.html', 'w', encoding='utf-8') as f:
    f.write(content)
