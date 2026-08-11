import re

with open('best-gallbladder-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    gb_html = f.read()

with open('hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    hr_html = f.read()

# Helper to extract a section by its ID
def extract_section(html, section_id):
    start_str = f'id="{section_id}"'
    # Find the <section tag that contains this id
    tag_start = html.rfind('<section ', 0, html.find(start_str))
    if tag_start == -1:
        # Maybe it's a different quote style or something, let's just regex
        match = re.search(r'(<section[^>]*id="' + section_id + r'".*?</section>)', html, re.DOTALL)
        if match: return match.group(1)
        return ""
    
    # manual extraction
    tag_count = 0
    in_section = False
    i = tag_start
    while i < len(html):
        if html[i:i+8] == '<section':
            tag_count += 1
            in_section = True
            i += 8
        elif html[i:i+10] == '</section>':
            tag_count -= 1
            if tag_count == 0 and in_section:
                return html[tag_start:i+10]
            i += 10
        else:
            i += 1
    return ""

diet_section = extract_section(gb_html, "diet")
cost_section = extract_section(gb_html, "cost")
faqs_section = extract_section(gb_html, "faqs")
appt_section = extract_section(gb_html, "appointment")

# Replace '.gb-' with '.hr-' in the copied sections to match conventions, though not strictly required
diet_section = diet_section.replace('gb-section', 'hr-section')
cost_section = cost_section.replace('gb-section', 'hr-section')
faqs_section = faqs_section.replace('gb-section', 'hr-section')
appt_section = appt_section.replace('gb-section', 'hr-section')

# Now adapt the text for Hernia!
# --- DIET SECTION ---
diet_section = diet_section.replace('Life After Gallbladder Removal: What to Eat', 'Life After Hernia Surgery: What to Eat & Recovery')
diet_section = diet_section.replace('After gallbladder removal, most patients can resume their diet fairly quickly. There are generally no specific long-term dietary restrictions imposed by the surgery itself. However, because your body needs time to adjust to the continuous trickle of bile into the intestines rather than a concentrated release, eating smaller, well-balanced meals is recommended.', 'After hernia repair, it is critical to avoid constipation and straining, as this puts pressure on the surgical mesh. A high-fiber diet rich in whole grains, fruits, and vegetables, along with plenty of water, ensures smooth bowel movements and protects your repair.')
diet_section = diet_section.replace('Moderating Fat Intake', 'High-Fiber & Hydration')
diet_section = diet_section.replace('In the first few weeks, it may be helpful to avoid large, extremely fatty, or greasy meals. Easing back into a normal diet allows the digestive system to adapt without causing temporary symptoms like bloating or loose stools.', 'Drinking plenty of water and consuming fiber-rich foods helps soften stool. You should avoid processed foods that cause bloating or constipation during the first few weeks of your recovery.')
diet_section = diet_section.replace('Gradual Reintroduction', 'Avoiding Heavy Straining')
diet_section = diet_section.replace('As your digestion normalizes, you can gradually reintroduce a wider variety of foods. Many patients find they can eventually eat the same healthy diet they enjoyed before surgery with no issues.', 'While walking is encouraged immediately, you must avoid heavy lifting, vigorous exercise, or strenuous activities for at least 4 to 6 weeks to allow the mesh to integrate strongly with your abdominal wall.')

# --- COST SECTION ---
cost_section = cost_section.replace('Laparoscopic and robotic gallbladder surgery', 'Laparoscopic and robotic hernioplasty')
cost_section = cost_section.replace('Laparoscopic & Robotic Gallbladder Packages', 'Laparoscopic & Robotic Hernia Packages')
cost_section = cost_section.replace('Standard package includes a 24-hour stay.', 'Packages vary based on unilateral/bilateral hernia or TAR requirements.')
cost_section = cost_section.replace('4K laparoscopic is standard. Robotic surgery or complex acute cases may alter the package.', '4K eTEP laparoscopy is standard. Robotic surgery utilizes specialized wristed instruments.')

# --- FAQS SECTION ---
# For FAQs, I will replace the Gallbladder questions with the Hernia questions from the original hr_html
hr_faqs_match = re.search(r'(<section class="hr-section hr-section--alt" id="faqs".*?</section>)', hr_html, re.DOTALL)
if hr_faqs_match:
    original_hr_faqs = hr_faqs_match.group(1)
    
    # We want to extract the Q&As from original_hr_faqs
    questions = re.findall(r'<span>(.*?)</span>', original_hr_faqs)
    answers = re.findall(r'<div class="hr-faq-answer">\s*<p>(.*?)</p>', original_hr_faqs, re.DOTALL)
    
    # Gallbladder faq structure has <details class="service-faq-item"> <summary><span>Q</span>...</summary> <div class="service-faq-ans"><p>A</p></div></details>
    # Reconstruct the FAQ list
    new_faq_list = ''
    for q, a in zip(questions, answers):
        new_faq_list += f'''
        <details class="service-faq-item">
          <summary>
            <span>{q.strip()}</span>
            <svg fill="none" height="20" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="20">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </summary>
          <div class="service-faq-ans">
            <p style="margin: 0;">{a.strip()}</p>
          </div>
        </details>
        '''
    
    # Replace the gallbladder FAQ list with the new one
    faqs_section = re.sub(r'<div class="service-faq-grid" style="margin-top: 3rem;">.*?</div>\s*</div>\s*</section>', f'<div class="service-faq-grid" style="margin-top: 3rem;">{new_faq_list}</div></div></section>', faqs_section, flags=re.DOTALL)
    
    # Also update the title/desc in FAQs
    faqs_section = faqs_section.replace('Everything you need to know about undergoing safe, keyhole gallbladder surgery with Dr. Atul Peters in Delhi NCR.', 'Everything you need to know about undergoing safe, permanent hernia reconstruction with Dr. Atul Peters in Delhi NCR.')

# --- APPT SECTION ---
# Nothing to adapt for Appointment, it's just a form. It says "gallbladder or hernia surgery" anyway probably, or just "Book your consultation".

# 3. Replace in hr_html
# Diet goes after recovery
hr_html = re.sub(r'(<section class="hr-section hr-section--alt" id="recovery".*?</section>)', r'\1\n\n' + diet_section, hr_html, flags=re.DOTALL)

# Replace Cost
hr_html = re.sub(r'<section class="hr-section" id="cost">.*?</section>', cost_section, hr_html, flags=re.DOTALL)

# Replace FAQs
hr_html = re.sub(r'<section class="hr-section hr-section--alt" id="faqs">.*?</section>', faqs_section, hr_html, flags=re.DOTALL)

# Replace Consult with Appt
hr_html = re.sub(r'<section class="hr-cta-section" id="consult">.*?</section>', appt_section, hr_html, flags=re.DOTALL)

with open('hernia-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(hr_html)

print("Replacement successful.")
