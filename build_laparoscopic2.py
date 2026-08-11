import re

with open('e:/atul-peters/atul-peters/laparoscopic-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix h2 title
html = re.sub(
    r'<h2 class="gb-section-title">4K Laparoscopic eTEP &amp; Da Vinci Robotic Surgery</h2>',
    '<h2 class="gb-section-title">4K Laparoscopic &amp; Da Vinci Robotic Surgery</h2>',
    html, flags=re.DOTALL
)

# Fix Standard IPOM Mesh / eTEP/TAR Protocol comparison section
# Let's change this to "Traditional Open Surgery" vs "Laparoscopic Approach"
html = re.sub(
    r'<h4><i class="fa-solid fa-triangle-exclamation"></i> Standard IPOM Mesh</h4>\s*<ul class="gb-compare-list bad">.*?</ul>',
    '''<h4><i class="fa-solid fa-triangle-exclamation"></i> Traditional Open Surgery</h4>
              <ul class="gb-compare-list bad">
                <li><i class="fa-solid fa-xmark"></i> Large, painful incisions</li>
                <li><i class="fa-solid fa-xmark"></i> Higher risk of wound infection</li>
                <li><i class="fa-solid fa-xmark"></i> Prolonged hospital stay</li>
                <li><i class="fa-solid fa-xmark"></i> Slower return to normal activities</li>
              </ul>''',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h4><i class="fa-solid fa-shield-check"></i> Dr\. Peters\' eTEP/TAR Protocol</h4>\s*<ul class="gb-compare-list good">.*?</ul>',
    '''<h4><i class="fa-solid fa-shield-check"></i> Dr. Peters\' Laparoscopic Approach</h4>
              <ul class="gb-compare-list good">
                <li><i class="fa-solid fa-check"></i> Tiny, virtually invisible keyhole incisions</li>
                <li><i class="fa-solid fa-check"></i> Significantly reduced risk of infection</li>
                <li><i class="fa-solid fa-check"></i> Discharge within 24-48 hours</li>
                <li><i class="fa-solid fa-check"></i> Rapid recovery and return to work</li>
              </ul>''',
    html, flags=re.DOTALL
)

# Remove the text "Dr. Peters’ zero-compromise approach ensures..." if it's there
html = re.sub(
    r'<p style="margin-top: 2rem; font-size: 1\.05rem; color: var\(--text-2\); line-height: 1\.6;">\s*Dr\. Peters’ zero-compromise approach ensures that mesh is placed exactly where nature intended.*?<br />\s*<strong style="color: var\(--blue-deep\);">Result: Less pain, shorter stay, and negligible recurrence\.</strong>\s*</p>',
    '''<p style="margin-top: 2rem; font-size: 1.05rem; color: var(--text-2); line-height: 1.6;">
              Dr. Peters’ zero-compromise approach ensures that surgeries are performed with the utmost precision using state-of-the-art technology.
              <br />
              <strong style="color: var(--blue-deep);">Result: Less pain, shorter stay, and a faster return to your normal life.</strong>
            </p>''',
    html, flags=re.DOTALL
)

with open('e:/atul-peters/atul-peters/laparoscopic-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(html)
