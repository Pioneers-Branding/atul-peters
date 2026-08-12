import re

html_path = r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update Procedure Overview (#symptoms) text
html = re.sub(
    r'<p class="gb-section-desc">.*?</p>',
    '<p class="gb-section-desc">First open gastric bypass was described by Mason and Ito in 1966. It has been modified into its current form using a Roux-en-Y limb of intestine (RYGB). The RYGB is one of the most commonly performed operations for weight loss all over the world, with the first laparoscopic gastric bypass performed by Wittgrove and Clark in 1994.</p>',
    html,
    count=1,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3>How Gastric Bypass Works</h3>.*?<div class="gb-highlight-box">',
    '<h3>Principle of Roux-en-Y Gastric Bypass</h3>\n          <p>Roux-en-Y Gastric bypass surgery is an operation in which a small pouch of stomach is created and joined to the small intestine after bypassing an initial segment of small intestine known as duodenum and jejunum, thereby diverting bile as well as intestinal secretions.</p>\n          <p><strong>Aim of this arrangement:</strong> To achieve long term weight loss with least side effects and complications, leading to resolution of obesity and its related comorbidities.</p>\n          <div class="gb-highlight-box">',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<p>This dramatically alters gut hormone signaling.*?reset the body\'s weight set-point\.</p>',
    '<p><strong>Mechanism of Weight Loss:</strong> The net effect is restricted intake of food and some malabsorption. Furthermore, altered gut hormones (ghrelin, GIP, GLP, PYY) reduce hunger and increase early satiety, modifying metabolism so that diabetes and blood pressure are resolved or controlled.</p>',
    html,
    flags=re.DOTALL
)

# Update Advanced Techniques (#technique) section
html = re.sub(
    r'<p class="gb-section-desc">A precise, minimally invasive surgery that creates a new pathway for digestion and absorption\. Performed via 4K Laparoscopic or Robotic approach\.</p>',
    '<p class="gb-section-desc"><strong>Surgical Aspects of Laparoscopic Roux-en-Y Gastric Bypass:</strong> A precise, minimally invasive surgery that creates a new pathway for digestion and absorption. Many studies done at Centers of Excellence all over the world report about 80% of excess weight loss.</p>',
    html,
    flags=re.DOTALL
)

# Update the 6 steps based on the text
html = re.sub(
    r'<h3><i class="fa-solid fa-user-check"></i> 1\. Preparation</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-user-check"></i> 1. Preparation</h3>\n            <p>Every patient is evaluated by a team of experts (physician, pulmonologist, cardiologist). Mandatory thromboembolism prophylaxis is given 6 to 12 hours before surgery.</p>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3><i class="fa-solid fa-scissors"></i> 2\. Incisions</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-scissors"></i> 2. Operating Ports</h3>\n            <p>Patient is placed in reverse Trendelenberg’s position. Usually 3 to 4 small operating incisions are made, closed by special glue with no stitches or bandages.</p>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3><i class="fa-solid fa-egg"></i> 3\. The Pouch</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-egg"></i> 3. Gastric Pouch</h3>\n            <p>The first step is the formation of a small gastric pouch by use of surgical staplers on a special tube called a gastric calibration tube.</p>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3><i class="fa-solid fa-route"></i> 4\. The Bypass</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-route"></i> 4. The Bypass</h3>\n            <p>About 100 to 170 cm of the small intestine is bypassed, diverting bile and intestinal secretions.</p>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3><i class="fa-solid fa-link"></i> 5\. Reconnection</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-link"></i> 5. Reconnection</h3>\n            <p>The intestines are re-attached to the stomach pouch by various mechanisms, like staplers or by suturing.</p>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<h3><i class="fa-solid fa-bed-pulse"></i> 6\. Recovery</h3>\s*<p>.*?</p>',
    '<h3><i class="fa-solid fa-bed-pulse"></i> 6. Results</h3>\n            <p>Marked improvements in quality of life, with resolution of type 2 diabetes, high blood pressure, cholesterol, and sleep apnea.</p>',
    html,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
