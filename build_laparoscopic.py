import re

with open('e:/atul-peters/atul-peters/laparoscopic-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Symptoms Section (Change to 'Benefits of Laparoscopic Surgery')
html = re.sub(
    r'<h3\s*style="font-family: \'Bellefair\', serif; font-size: 2rem; color: var\(--blue-deep\); margin-bottom: 1rem; display: flex; align-items: center; gap: 0\.75rem;">\s*<i class="fa-solid fa-triangle-exclamation" style="color: #E53E3E;"></i> Warning Signs\s*</h3>\s*<p style="color: var\(--text-2\); font-size: 1\.05rem; margin-bottom: 2rem; line-height: 1\.6;">Many gallstones\s*remain silent for years\. However, when a stone moves and temporarily blocks the cystic duct during\s*digestion, it triggers intense episodes of biliary colic and inflammation\.</p>',
    '''<h3 style="font-family: 'Bellefair', serif; font-size: 2rem; color: var(--blue-deep); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;">
            <i class="fa-solid fa-leaf" style="color: #38A169;"></i> The Minimally Invasive Solution
          </h3>
          <p style="color: var(--text-2); font-size: 1.05rem; margin-bottom: 2rem; line-height: 1.6;">Laparoscopic surgery innovatively enables doctors to diagnose and treat diseases within the abdomen or pelvis without large incisions. The tip of the laparoscope is equipped with a high-definition camera to ensure real-time monitoring and unprecedented precision.</p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="symptom-item">\s*<div class="symptom-icon"><i class="fa-solid fa-bolt"></i></div>\s*<div>\s*<strong style="color: var\(--text-1\); font-size: 1\.1rem; display: block; margin-bottom: 0\.25rem;">Sharp\s*Right Pain</strong>\s*<p style="font-size: 0\.95rem; margin:0; color: var\(--text-2\);">Sudden, cramping pain under the right rib\s*cage radiating to the back or right shoulder\.</p>\s*</div>\s*</div>',
    '''<div class="symptom-item">
              <div class="symptom-icon"><i class="fa-solid fa-compress-arrows-alt"></i></div>
              <div>
                <strong style="color: var(--text-1); font-size: 1.1rem; display: block; margin-bottom: 0.25rem;">Less Tissue Damage</strong>
                <p style="font-size: 0.95rem; margin:0; color: var(--text-2);">Significantly reduced trauma within your abdominal cavity compared to open surgeries.</p>
              </div>
            </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="symptom-item">\s*<div class="symptom-icon"><i class="fa-solid fa-utensils"></i></div>\s*<div>\s*<strong\s*style="color: var\(--text-1\); font-size: 1\.1rem; display: block; margin-bottom: 0\.25rem;">Post-Meal\s*Attacks</strong>\s*<p style="font-size: 0\.95rem; margin:0; color: var\(--text-2\);">Severe discomfort typically triggered\s*30-60 mins after eating oily, fried, or high-fat meals\.</p>\s*</div>\s*</div>',
    '''<div class="symptom-item">
              <div class="symptom-icon"><i class="fa-solid fa-droplet-slash"></i></div>
              <div>
                <strong style="color: var(--text-1); font-size: 1.1rem; display: block; margin-bottom: 0.25rem;">Minimal Blood Loss</strong>
                <p style="font-size: 0.95rem; margin:0; color: var(--text-2);">Precise instrumentation ensures reduced risk of hemorrhage and bleeding.</p>
              </div>
            </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="symptom-item">\s*<div class="symptom-icon"><i class="fa-solid fa-face-dizzy"></i></div>\s*<div>\s*<strong style="color: var\(--text-1\); font-size: 1\.1rem; display: block; margin-bottom: 0\.25rem;">Nausea\s*&amp; Bloating</strong>\s*<p style="font-size: 0\.95rem; margin:0; color: var\(--text-2\);">Persistent indigestion, heavy gas,\s*heartburn, and episodes of vomiting\.</p>\s*</div>\s*</div>',
    '''<div class="symptom-item">
              <div class="symptom-icon"><i class="fa-solid fa-shield-virus"></i></div>
              <div>
                <strong style="color: var(--text-1); font-size: 1.1rem; display: block; margin-bottom: 0.25rem;">Fewer Risks of Infection</strong>
                <p style="font-size: 0.95rem; margin:0; color: var(--text-2);">Smaller incisions naturally decrease the likelihood of postoperative infections and scarring.</p>
              </div>
            </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="symptom-item">\s*<div class="symptom-icon"><i class="fa-solid fa-temperature-arrow-up"></i></div>\s*<div>\s*<strong style="color: var\(--text-1\); font-size: 1\.1rem; display: block; margin-bottom: 0\.25rem;">Fever\s*&amp; Chills</strong>\s*<p style="font-size: 0\.95rem; margin:0; color: var\(--text-2\);">Indicates acute bacterial infection and\s*inflammation \(Incarcerated Conditions\)\.</p>\s*</div>\s*</div>',
    '''<div class="symptom-item">
              <div class="symptom-icon"><i class="fa-solid fa-person-running"></i></div>
              <div>
                <strong style="color: var(--text-1); font-size: 1.1rem; display: block; margin-bottom: 0.25rem;">Faster Recovery</strong>
                <p style="font-size: 0.95rem; margin:0; color: var(--text-2);">Less time in the hospital translates to faster return to life with a normal schedule.</p>
              </div>
            </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="gb-highlight-box"\s*style="margin-top: 1\.5rem; background: #FFF5F5; border: 1px solid #FED7D7; color: #C53030; display: inline-block;">\s*<p style="margin: 0; font-weight: 500;"><i class="fa-solid fa-circle-info"></i> Never ignore repeated\s*abdominal cramps after fatty meals\. Early diagnosis prevents emergency biliary attacks\.</p>\s*</div>',
    '''<div class="gb-highlight-box" style="margin-top: 1.5rem; background: #F0FFF4; border: 1px solid #C6F6D5; color: #276749; display: inline-block; padding: 1rem; border-radius: 0.5rem;">
            <p style="margin: 0; font-weight: 500;"><i class="fa-solid fa-circle-check"></i> Choose Laparoscopy: A modern approach leaning towards faster recovery, fewer dissections, and minimal complications.</p>
          </div>''',
    html, flags=re.DOTALL
)

# 2. Risk & Diagnosis -> Common Surgeries
html = re.sub(
    r'<h3\s*style="font-family: \'Bellefair\', serif; font-size: 2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0\.75rem;">\s*<i class="fa-solid fa-stethoscope" style="color: #A8DECE;"></i> Risk &amp; Diagnosis\s*</h3>\s*<p style="font-size: 1\.05rem; opacity: 0\.9; margin-bottom: 1rem; line-height: 1\.6; position: relative;">\s*Laparoscopic surgery is used for various conditions\. Here are the common presentations\.\s*</p>',
    '''<h3 style="font-family: 'Bellefair', serif; font-size: 2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;">
              <i class="fa-solid fa-briefcase-medical" style="color: #A8DECE;"></i> Common Procedures
            </h3>
            <p style="font-size: 1.05rem; opacity: 0.9; margin-bottom: 1rem; line-height: 1.6; position: relative;">
              Delhi is a global destination for patients seeking specialized minimally invasive procedures. Dr. Peters specializes in:
            </p>''',
    html, flags=re.DOTALL
)

# Four-f Grid Replacement
html = re.sub(
    r'<div class="four-f-grid">\s*<div class="four-f-item" style="position: relative;">\s*<div class="four-f-letter">F</div>\s*<div class="four-f-text">Inguinal</div>\s*<div style="font-size: 0\.8rem; opacity: 0\.8; margin-top: 0\.25rem;">Inner groin area</div>\s*</div>\s*<div class="four-f-item">\s*<div class="four-f-letter">F</div>\s*<div class="four-f-text">Umbilical</div>\s*<div style="font-size: 0\.8rem; opacity: 0\.8; margin-top: 0\.25rem;">Belly button area</div>\s*</div>\s*<div class="four-f-item">\s*<div class="four-f-letter">F</div>\s*<div class="four-f-text">Incisional</div>\s*<div style="font-size: 0\.8rem; opacity: 0\.8; margin-top: 0\.25rem;">Previous scar site</div>\s*</div>\s*<div class="four-f-item">\s*<div class="four-f-letter">F</div>\s*<div class="four-f-text">Ventral</div>\s*<div style="font-size: 0\.8rem; opacity: 0\.8; margin-top: 0\.25rem;">Upper abdomen wall</div>\s*</div>\s*</div>\s*<p style="font-size: 0\.95rem; opacity: 0\.85; margin-bottom: 2rem; text-align: center;">Waiting for emergency surgery leads to progressive risk\.</p>',
    '''<div class="four-f-grid">
              <div class="four-f-item" style="position: relative;">
                <div class="four-f-letter">A</div>
                <div class="four-f-text">Appendectomy</div>
                <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.25rem;">Removal of inflamed appendix</div>
              </div>
              <div class="four-f-item">
                <div class="four-f-letter">G</div>
                <div class="four-f-text">Gallbladder</div>
                <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.25rem;">Cholecystectomy</div>
              </div>
              <div class="four-f-item">
                <div class="four-f-letter">H</div>
                <div class="four-f-text">Hernia Repair</div>
                <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.25rem;">Inguinal, Umbilical, Ventral</div>
              </div>
              <div class="four-f-item">
                <div class="four-f-letter">B</div>
                <div class="four-f-text">Bariatric</div>
                <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.25rem;">Weight Loss Surgeries</div>
              </div>
            </div>
            <p style="font-size: 0.95rem; opacity: 0.85; margin-bottom: 2rem; text-align: center;">Advancements and high success rates make Delhi a surgical capital.</p>''',
    html, flags=re.DOTALL
)

# Diagnostic Box
html = re.sub(
    r'<i class="fa-solid fa-microscope" style="font-size: 1\.5rem; color: #3182ce; margin-top: 0\.2rem;"></i>\s*<div>\s*<h4\s*style="margin: 0 0 0\.25rem 0; font-family: \'DM Sans\', sans-serif; font-size: 1\.1rem; color: var\(--text-1\);">\s*Diagnostic Precision</h4>\s*<p style="margin: 0; font-size: 0\.95rem; color: var\(--text-2\); line-height: 1\.5;">A simple physical examination is usually sufficient\. We may utilize a <strong>High-Resolution Ultrasound or CT Scan</strong> to map complex or recurrent abdominal wall defects\.\s*</p>\s*</div>',
    '''<i class="fa-solid fa-shield-halved" style="font-size: 1.5rem; color: #3182ce; margin-top: 0.2rem;"></i>
              <div>
                <h4 style="margin: 0 0 0.25rem 0; font-family: 'DM Sans', sans-serif; font-size: 1.1rem; color: var(--text-1);">
                  Safe &amp; Effective</h4>
                <p style="margin: 0; font-size: 0.95rem; color: var(--text-2); line-height: 1.5;">Laparoscopy is generally a very safe technique. Risks are minimal as the surgeon is visually aided by real-time 4K monitoring and precise operative measures.
                </p>
              </div>''',
    html, flags=re.DOTALL
)

# Technique Section
html = re.sub(
    r'<h3 class="tech-title">4K HD Laparoscopic eTEP</h3>\s*<p class="tech-desc">Through 4 tiny keyholes \(less than half an inch\), a high-definition 4K camera and\s*specialized micro-instruments are introduced\. The defect is closed and a large mesh is placed extraperitoneally\.</p>',
    '''<h3 class="tech-title">4K HD Laparoscopic Surgery</h3>
          <p class="tech-desc">Through tiny keyholes (less than half an inch), a high-definition 4K camera and specialized micro-instruments are introduced. This allows for intricate surgeries like gallbladder or appendix removal with unmatched clarity.</p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h3 class="tech-title">Da Vinci Robotic TAR</h3>\s*<p class="tech-desc">For complex anatomical situations—such as massive incisional hernias or loss of domain—the advanced Da Vinci Xi Robotic System provides 3D high-definition magnified optics and 360-degree\s*wristed articulation\.</p>',
    '''<h3 class="tech-title">Da Vinci Robotic Surgery</h3>
          <p class="tech-desc">For complex procedures, the advanced Da Vinci Xi Robotic System provides 3D high-definition magnified optics and 360-degree wristed articulation, giving the surgeon greater flexibility and control.</p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<li><i class="fa-solid fa-check-circle"></i> Unparalleled precision for transversus abdominis release \(TAR\)</li>',
    '''<li><i class="fa-solid fa-check-circle"></i> Better outcomes, less pain, and quicker recovery</li>''',
    html, flags=re.DOTALL
)

# Infographic Section (The Muscular Defect, etc.)
html = re.sub(
    r'<h4>The Muscular Defect</h4>\s*<p>The core issue is a physical hole in the strong fascial layer of your abdomen\. Intestines or fat push through this gap, creating the visible bulge under your skin\.</p>',
    '''<h4>Minimally Invasive</h4>
                <p>Instead of a large, painful open cut, laparoscopic surgery relies on small keyhole incisions, minimizing tissue damage and reducing postoperative pain significantly.</p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h4>Standard IPOM \(Old Method\)</h4>\s*<p>Historically, mesh was placed directly inside the peritoneal cavity \(IPOM\), touching the bowels\. This risked dangerous adhesions, chronic pain, and bowel fistulas\.</p>',
    '''<h4>High-Definition Clarity</h4>
                <p>A laparoscope equipped with a high-definition camera is inserted, projecting the internal anatomy onto a screen in real-time, allowing the surgeon unparalleled visibility.</p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h4>eTEP / TAR \(Modern Standard\)</h4>\s*<p>Dr\. Peters utilizes the eTEP technique, placing the mesh outside the peritoneal cavity between muscle layers\. This guarantees ZERO mesh-to-bowel contact and < 1% recurrence\.</p>',
    '''<h4>Dr. Peters\' Expertise</h4>
                <p>Utilizing both single-incision laparoscopic surgery (SILS) and the ERAS protocol, Dr. Peters ensures swift operations with fewer complications and an accelerated recovery timeline.</p>''',
    html, flags=re.DOTALL
)

# Critical View of Safety Section (Change to ERAS Protocol / General Safety)
html = re.sub(
    r'<h3 class="cvs-title">The "Critical View of Safety"</h3>\s*<p class="cvs-desc">\s*Before any cut is made to the cystic duct or artery, Dr\. Peters achieves a mandatory 360-degree view of the anatomy\. This protocol ensures zero bile duct injuries, maximizing patient safety\.\s*</p>',
    '''<h3 class="cvs-title">The ERAS Protocol for Recovery</h3>
            <p class="cvs-desc">
              Enhanced Recovery After Surgery (ERAS) is an umbrella term for comprehensive sets of care procedures thought to reduce postoperative pain &amp; nausea and ensure speedy recovery.
            </p>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="cvs-text">\s*<h4>Clear Identification</h4>\s*<p>The cystic duct and artery are completely separated from surrounding tissue before clipping\.</p>\s*</div>',
    '''<div class="cvs-text">
                  <h4>Reduced Postoperative Pain</h4>
                  <p>Minimizing tissue trauma ensures patients experience significantly less pain compared to traditional open surgeries.</p>
                </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="cvs-text">\s*<h4>Liver Bed Exposure</h4>\s*<p>The lower part of the gallbladder is cleanly separated from the liver bed to guarantee proper orientation\.</p>\s*</div>',
    '''<div class="cvs-text">
                  <h4>Shorter Hospital Stays</h4>
                  <p>Less time in the hospital translates to better and faster recovery, getting you back to your normal life quicker.</p>
                </div>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="cvs-text">\s*<h4>The \"Two Structures\" Rule</h4>\s*<p>Only two structures \(the duct and the artery\) are seen entering the gallbladder\.</p>\s*</div>',
    '''<div class="cvs-text">
                  <h4>Fewer Complications</h4>
                  <p>Smaller incisions inherently reduce the risk of surgical site infections and postoperative hernias.</p>
                </div>''',
    html, flags=re.DOTALL
)


with open('e:/atul-peters/atul-peters/laparoscopic-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(html)
