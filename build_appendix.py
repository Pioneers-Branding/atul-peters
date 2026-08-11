import re

with open('hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
html = html.replace('<title>Best Hernia Surgery in Delhi | Laparoscopic &amp; Robotic eTEP Specialist</title>', '<title>Best Appendix Surgery in Delhi | Laparoscopic Appendectomy | Dr. Atul Peters</title>')
html = html.replace('content="Seeking expert hernia surgery in Delhi? Consult Dr. Atul Peters at Max Smart Super Speciality Hospital. Advanced Laparoscopic & Robotic eTEP / TAR repair for hernias with < 1% recurrence and 24-hr discharge."', 'content="Seeking expert appendix surgery in Delhi? Consult Dr. Atul Peters at Max Smart Super Speciality Hospital. Advanced Laparoscopic Appendectomy for appendicitis with virtually invisible scars and rapid 24-hour discharge."')
html = html.replace('content="hernia surgery in Delhi, laparoscopic hernia repair Delhi, eTEP hernia surgery India, robotic hernia repair Delhi NCR, inguinal hernia specialist Delhi, Dr Atul Peters"', 'content="appendix surgery in Delhi, laparoscopic appendectomy Delhi, appendicitis treatment India, inflamed appendix removal Delhi NCR, best appendix surgeon Delhi, Dr Atul Peters"')
html = html.replace('href="https://www.atulpeters.com/hernia-surgery-in-delhi"', 'href="https://www.atulpeters.com/best-appendix-surgery-in-delhi-india"')
html = html.replace('content="Best Hernia Surgery in Delhi | Dr. Atul Peters"', 'content="Best Appendix Surgery in Delhi | Dr. Atul Peters"')
html = html.replace('content="Experience safe, painless, gold-standard keyhole hernia reconstruction in Delhi with Dr. Atul Peters. 4K Ultra HD visualization, Critical View of Safety protocols, and overnight recovery."', 'content="Experience safe, painless, gold-standard laparoscopic appendectomy in Delhi with Dr. Atul Peters. Minimally invasive removal of the inflamed appendix with overnight recovery."')
html = html.replace('content="https://www.atulpeters.com/assets/img/Hernia-Gallbladder-Surgery.webp"', 'content="https://www.atulpeters.com/assets/img/Appendix-Surgery.webp"')

# 2. Hero Section
html = html.replace('Best Hernia Surgery in <span>Delhi NCR</span>', 'Best Appendix Surgery in <span>Delhi NCR</span>')
html = html.replace('<strong>Laparoscopic &amp; Robotic eTEP Hernia Repair</strong>', '<strong>Laparoscopic Appendectomy (Appendix Removal)</strong>')
html = html.replace('Advanced Extraperitoneal Mesh • < 1% Recurrence', 'Minimally Invasive Keyhole Surgery • 24-Hour Discharge')
html = html.replace('Sub-lay Mesh Placement', 'Safe Organ Removal')
html = html.replace('sketch_hernia_surgeon_1785910965814.png', 'sketch_appendix_surgeon_1785927623986.png')

# 3. Quick Nav
html = html.replace('href="#overview">Hernia Overview</a>', 'href="#overview">Appendix Overview</a>')
html = html.replace('href="#types">Types &amp; Symptoms</a>', 'href="#types">Warning Symptoms</a>')
html = html.replace('href="#safety">Advanced Techniques</a>', 'href="#safety">Advanced Techniques</a>')
html = html.replace('href="#danger">Complications</a>', 'href="#danger">Rupture Risks</a>')
html = html.replace('href="#journey">Recovery Timeline</a>', 'href="#journey">Recovery Timeline</a>')
html = html.replace('href="#diet">Diet &amp; Activities</a>', 'href="#diet">Diet &amp; Activities</a>')

# 4. Overview Section
html = html.replace('What is a Hernia?', 'What is Appendicitis?')
html = html.replace('A hernia occurs when an internal organ pushes through a weak spot in your muscle or tissue. Unlike a cold, a hernia will not heal on its own.', 'Appendicitis is a sudden and painful inflammation of the appendix, a small finger-shaped pouch attached to your large intestine. When it becomes blocked and infected, it requires urgent surgical removal.')
html = html.replace('It acts like a tire bulging through a tear in the outer wall. If left untreated, it can lead to severe pain and life-threatening complications like bowel strangulation.', 'If left untreated, an inflamed appendix can burst (rupture) within 48 to 72 hours, spreading dangerous infection throughout your abdomen (peritonitis), which can be life-threatening.')
html = html.replace('sketch_hernia_defect_1785910910586.png', 'sketch_appendix_overview_1785927635175.png')
html = html.replace('Anatomical sketch of a hernia defect', 'Anatomical sketch of an inflamed appendix')

# 5. Types / Symptoms Section
html = html.replace('<span class="gb-section-tag">Anatomy</span>', '<span class="gb-section-tag">Warning Signs</span>')
html = html.replace('<h2 class="gb-section-title">Common Types of Hernia</h2>', '<h2 class="gb-section-title">Common Symptoms of Appendicitis</h2>')
html = html.replace('Not all hernias are the same. Identifying the specific type helps determine the best surgical approach for a permanent repair.', 'Appendicitis typically starts with a vague pain near the belly button that eventually shifts to the lower right abdomen. Early detection is critical.')

# Replace the 4 cards in the types section
html = html.replace('''<h3 class="gb-card-title">Inguinal Hernia</h3>
            <p class="gb-card-desc">The most common type, occurring in the inner groin canal. Mostly affects men.</p>''', '''<h3 class="gb-card-title">Lower Right Abdominal Pain</h3>
            <p class="gb-card-desc">The classic symptom: sharp pain that starts around the navel and migrates to the lower right side.</p>''')
html = html.replace('''<h3 class="gb-card-title">Ventral/Umbilical Hernia</h3>
            <p class="gb-card-desc">Occurs near the belly button or along the midline of the abdomen.</p>''', '''<h3 class="gb-card-title">Nausea &amp; Vomiting</h3>
            <p class="gb-card-desc">Often accompanies the abdominal pain, along with a sudden loss of appetite.</p>''')
html = html.replace('''<h3 class="gb-card-title">Incisional Hernia</h3>
            <p class="gb-card-desc">Develops at the site of a previous surgical scar due to weakened tissue.</p>''', '''<h3 class="gb-card-title">Low-Grade Fever</h3>
            <p class="gb-card-desc">A mild fever that may worsen as the infection progresses and inflammation increases.</p>''')
html = html.replace('''<h3 class="gb-card-title">Hiatal Hernia</h3>
            <p class="gb-card-desc">Upper stomach bulges through the diaphragm, causing severe acid reflux.</p>''', '''<h3 class="gb-card-title">Rebound Tenderness</h3>
            <p class="gb-card-desc">Severe pain when pressure is suddenly released from the lower right abdomen.</p>''')
            
html = html.replace('sketch_hernia_types_1785910928121.png', 'sketch_appendix_symptoms_1785927647316.png')

# 6. Safety / Advanced Techniques
html = html.replace('<span class="gb-section-tag">Advanced Surgical Options</span>', '<span class="gb-section-tag">Advanced Surgical Options</span>')
html = html.replace('<h2 class="gb-section-title">Laparoscopic eTEP &amp; Robotic Hernia Repair</h2>', '<h2 class="gb-section-title">Laparoscopic Appendectomy</h2>')
html = html.replace('Dr. Atul Peters specializes in the highly advanced <strong>eTEP (Extended-View Totally Extraperitoneal)</strong> and <strong>TAR</strong> techniques. Instead of open surgery, the repair is done through 3 tiny keyholes.', 'Dr. Atul Peters specializes in <strong>Laparoscopic Appendectomy</strong>. Instead of a large open incision, the infected appendix is safely removed through 3 tiny keyhole incisions.')
html = html.replace('The mesh is placed strictly in the <em>sub-lay retro-muscular space</em>, meaning it never touches your intestines. This ensures zero bowel adhesions, dramatically less pain, and a recurrence rate of less than 1%.', 'This minimally invasive approach offers a superior view of the abdomen, drastically reduces post-operative pain, lowers the risk of wound infection, and ensures you can return home within 24 hours with virtually invisible scars.')
html = html.replace('sketch_hernia_mesh_placement_1785910946322.png', 'sketch_appendix_laparoscopic_1785927658976.png')

html = html.replace('<div class="gb-feature-title">No Bowel Contact</div>', '<div class="gb-feature-title">No Large Scars</div>')
html = html.replace('<div class="gb-feature-desc">Extraperitoneal mesh placement prevents dangerous intestinal adhesions.</div>', '<div class="gb-feature-desc">Only 3 tiny 5mm incisions compared to a traditional 4-inch open scar.</div>')
html = html.replace('<div class="gb-feature-title">&lt; 1% Recurrence</div>', '<div class="gb-feature-title">Rapid Recovery</div>')
html = html.replace('<div class="gb-feature-desc">The muscles clamp down on the mesh naturally, making it permanent.</div>', '<div class="gb-feature-desc">Most patients are walking the same day and discharged within 24 hours.</div>')
html = html.replace('<div class="gb-feature-title">Micro-Incisions</div>', '<div class="gb-feature-title">Reduced Infection Risk</div>')
html = html.replace('<div class="gb-feature-desc">Avoids the massive scars and chronic nerve pain of open surgery.</div>', '<div class="gb-feature-desc">Laparoscopy drastically minimizes the risk of post-operative wound infections.</div>')


# 7. Danger
html = html.replace('<span class="gb-section-tag">The Hidden Dangers</span>', '<span class="gb-section-tag">The Hidden Dangers</span>')
html = html.replace('<h2 class="gb-section-title">The Risk of Incarceration &amp; Strangulation</h2>', '<h2 class="gb-section-title">The Risk of a Ruptured Appendix</h2>')
html = html.replace('A hernia is a mechanical defect—it will never heal with medicine or exercise. If ignored, the hole will continue to enlarge.', 'Appendicitis is a medical emergency. You cannot cure an infected appendix with antibiotics alone or home remedies.')
html = html.replace('The greatest danger is <strong>Strangulation</strong>. This occurs when a loop of intestine gets trapped in the hernia defect, cutting off its blood supply. This causes gangrene (tissue death) within hours and requires emergency, life-saving surgery.', 'The greatest danger is a <strong>Ruptured Appendix</strong>. If surgery is delayed, the swollen appendix can burst, spilling infectious pus and bacteria into the abdominal cavity. This causes a life-threatening condition called Peritonitis, which requires emergency surgery and a prolonged hospital stay.')
html = html.replace('sketch_hernia_danger_stages_1785910919540.png', 'sketch_appendix_danger_1785927669702.png')

# 8. CTA
html = html.replace('Don\'t Wait for a Hernia Emergency', 'Don\'t Wait for an Appendix Emergency')
html = html.replace('Elective hernia repair is a safe, routine 45-minute procedure with overnight discharge. Emergency surgery for a strangulated hernia is highly complex and carries significant risks.', 'Early laparoscopic removal is a safe, routine 30-minute procedure with overnight discharge. A ruptured appendix requires complex surgery and high-risk recovery.')

# 9. Recovery Journey
html = html.replace('<h2 class="gb-section-title">Your 24-Hour Hernia Surgery Journey</h2>', '<h2 class="gb-section-title">Your 24-Hour Appendix Surgery Journey</h2>')
html = html.replace('We combine Enhanced Recovery After Surgery (ERAS) pathways with compassionate hospital care to ensure your hernia repair is smooth and painless.', 'We combine Enhanced Recovery After Surgery (ERAS) pathways with compassionate hospital care to ensure your appendix removal is smooth and painless.')
html = html.replace('sketch_patient_walking_1785910955832.png', 'sketch_appendix_recovery_1785927682071.png')

html = html.replace('<h4 class="gb-timeline-title">Admission &amp; Evaluation</h4>', '<h4 class="gb-timeline-title">Admission &amp; Evaluation</h4>')
html = html.replace('<p class="gb-timeline-desc">Fast-track admission. Vitals are checked, and a brief anesthetic consultation ensures you are fully prepared.</p>', '<p class="gb-timeline-desc">Immediate admission. Blood tests and an ultrasound or CT scan are done to confirm appendicitis.</p>')
html = html.replace('<h4 class="gb-timeline-title">The eTEP Surgery</h4>', '<h4 class="gb-timeline-title">The Laparoscopic Surgery</h4>')
html = html.replace('<p class="gb-timeline-desc">Dr. Peters performs the minimally invasive keyhole repair and mesh placement. The procedure typically lasts 45 to 90 minutes.</p>', '<p class="gb-timeline-desc">Dr. Peters performs the minimally invasive keyhole removal of the appendix. The procedure typically lasts 30 to 45 minutes.</p>')
html = html.replace('<p class="gb-timeline-desc">You will be gently woken up. By evening, you will be encouraged to walk around your room to promote circulation.</p>', '<p class="gb-timeline-desc">You will be gently woken up. By evening, you will be encouraged to walk around your room to promote circulation.</p>')

# 10. Diet Section
html = html.replace('Post-Surgery Diet &amp; Care', 'Post-Surgery Diet &amp; Care')
html = html.replace('Following our ERAS protocol, your recovery at home will be surprisingly fast. Here is what to expect in the days after your hernia repair.', 'Following our ERAS protocol, your recovery at home will be surprisingly fast. Here is what to expect in the days after your appendix removal.')

html = html.replace('Do not lift anything heavier than 5kg for 4 weeks. This allows the mesh to integrate securely into your abdominal muscles.', 'Do not lift anything heavier than 5kg for 2-3 weeks to allow your abdominal muscles to heal properly.')
html = html.replace('You may experience a tight or pulling sensation around the mesh area for a few weeks. This is normal healing, not the hernia returning.', 'You may experience some bloating or shoulder pain for a few days due to the carbon dioxide gas used during laparoscopy. This is perfectly normal.')
html = html.replace('Return to office work or driving is usually permitted within 5 to 7 days, depending on your comfort level.', 'Return to office work, school, or driving is usually permitted within 3 to 7 days, depending on your comfort level.')

# 11. FAQ
html = html.replace('<h2 class="gb-section-title">Hernia Surgery FAQs</h2>', '<h2 class="gb-section-title">Appendix Surgery FAQs</h2>')

html = html.replace('Can a hernia be cured without surgery?', 'Can appendicitis be cured with antibiotics instead of surgery?')
html = html.replace('''No. A hernia is a physical tear or hole in your muscle wall. No medication, belt, or exercise can close this gap. Surgical repair is the only permanent cure.''', '''While some mild cases of appendicitis have been treated with antibiotics alone in experimental settings, the international gold standard remains surgical removal. Antibiotic-only treatment has a high recurrence rate (the appendicitis comes back), and surgery is the only definitive, permanent cure.''')

html = html.replace('Is a hernia dangerous?', 'Is appendicitis always an emergency?')
html = html.replace('''While small hernias might just be uncomfortable, they are unpredictable. A loop of intestine can suddenly become trapped in the hole (incarceration). If the blood supply is cut off (strangulation), it becomes a life-threatening emergency within hours.''', '''Yes. Once the appendix is infected and blocked, the inflammation progresses rapidly. If not surgically removed, the organ can burst within 48-72 hours, spreading a deadly infection throughout the abdomen.''')

html = html.replace('Will I feel the mesh inside me?', 'Will my body function normally without an appendix?')
html = html.replace('''Modern lightweight meshes are incredibly flexible and biocompatible. While you may feel a tight sensation during the first few weeks of healing, the mesh eventually becomes fully integrated with your tissue, and you won't feel it at all.''', '''Yes, perfectly normal. The appendix is considered a vestigial organ (it has no major essential function in older children and adults). Removing it will not affect your digestion, immune system, or long-term health in any way.''')

html = html.replace('How long does the surgery take?', 'How long does the surgery take?')
html = html.replace('''An uncomplicated laparoscopic eTEP repair typically takes 45 to 90 minutes. Complex abdominal wall reconstructions or massive incisional hernias may take longer.''', '''A routine laparoscopic appendectomy typically takes only 30 to 45 minutes. If the appendix has already ruptured, the surgery takes longer to thoroughly clean the abdominal cavity.''')

# Write output
with open('best-appendix-surgery-in-delhi-india.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Appendix page successfully generated!")
