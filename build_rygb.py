import re

with open(r'e:\atul-peters\atul-peters\hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    hernia_html = f.read()

with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'r', encoding='utf-8') as f:
    rygb_html = f.read()

# Extract SEO JSON-LD from RYGB
seo_matches = re.findall(r'(<script type="application/ld\+json">.*?</script>)', rygb_html, flags=re.DOTALL)
rygb_seo = "\n".join(seo_matches)

new_html = hernia_html

# --- HEAD REPLACEMENTS ---
new_html = re.sub(
    r'<title>.*?</title>',
    '<title>Roux-en-Y Gastric Bypass Surgery Delhi | RYGB Cost, Risks &amp; Recovery | Dr. Atul Peters</title>',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta\s+content="Seeking the best gallbladder surgery in Delhi.*?"\s+name="description"\s*/>',
    '<meta content="Roux-en-Y Gastric Bypass (RYGB) in Delhi by Dr. Atul Peters at Max Smart Super Speciality Hospital. ~80% excess weight loss, 85% Type 2 Diabetes remission." name="description" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta\s+content="best gallbladder surgery in Delhi.*?"\s+name="keywords"\s*/>',
    '<meta content="Roux-en-Y gastric bypass Delhi, RYGB surgery India, gastric bypass cost Delhi, weight loss surgery Delhi, metabolic surgery" name="keywords" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<link href="https://www.atulpeters.com/hernia-surgery-in-delhi" rel="canonical" />',
    '<link href="https://www.atulpeters.com/roux-en-y-gastric-bypass.html" rel="canonical" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta content="Best Gallbladder Surgery in Delhi.*?"\s+property="og:title"\s*/>',
    '<meta content="Roux-en-Y Gastric Bypass in Delhi | Dr. Atul Peters" property="og:title" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta\s+content="Experience safe, painless, gold-standard keyhole hernia reconstruction.*?"\s+property="og:description"\s*/>',
    '<meta content="The Gold Standard bariatric surgery. ~80% excess weight loss, resolves Type 2 Diabetes. Performed laparoscopically or with robotic precision." property="og:description" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta content="https://www\.atulpeters\.com/best-gallbladder-surgery-in-delhi" property="og:url" />',
    '<meta content="https://www.atulpeters.com/roux-en-y-gastric-bypass.html" property="og:url" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta content="Dr\. Atul Peters — Bariatric, Minimal Access &amp; Robotic Surgery" property="og:site_name" />',
    '<meta content="Dr. Atul Peters — Bariatric &amp; Metabolic Surgery" property="og:site_name" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta content="Best Hernia Surgery in Delhi \| Dr\. Atul Peters" name="twitter:title" />',
    '<meta content="Roux-en-Y Gastric Bypass Surgery Delhi | Dr. Atul Peters" name="twitter:title" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<meta\s+content="Gold standard 4K laparoscopic and robotic hernia reconstruction surgery.*?"\s+name="twitter:description"\s*/>',
    '<meta content="Gold Standard bariatric surgery at Max Smart Super Speciality Hospital. ~80% EWL, 85% diabetes remission." name="twitter:description" />',
    new_html, flags=re.DOTALL
)
new_html = re.sub(
    r'<script type="application/ld\+json">.*?</script>.*?(?=</head>)',
    rygb_seo + '\n',
    new_html, flags=re.DOTALL
)

# Remove the sketch background entirely or replace it
new_html = re.sub(
    r'background-image: url\(\'assets/img/sketch_hernia_surgeon_1785910965814\.png\'\)',
    "background-image: none",
    new_html
)
new_html = re.sub(
    r'background-image: url\(\'assets/img/sketch_hernia_defect_1785910910586\.png\'\)',
    "background-image: none",
    new_html
)

# --- HERO SECTION ---
new_html = new_html.replace(
    '<span class="nc-breadcrumb-current">Best Gallbladder Surgery in Delhi</span>',
    '<span class="nc-breadcrumb-current">Roux-en-Y Gastric Bypass</span>'
)
new_html = new_html.replace(
    '<a href="other-surgeries/laparoscopic-hernia.html">Other Surgeries</a>',
    '<a href="weight-loss.html">Weight Loss</a>'
)
new_html = new_html.replace(
    'Advanced Extraperitoneal Mesh • < 1% Recurrence',
    'The Gold Standard • Since 1966'
)
new_html = re.sub(
    r'<h1 class="gb-hero-title">Best Hernia Surgery in <span>Delhi NCR</span></h1>',
    '<h1 class="gb-hero-title">Roux-en-Y <br/><span>Gastric Bypass</span></h1>',
    new_html
)
new_html = re.sub(
    r'<p class="gb-hero-subtitle">.*?</p>',
    '<p class="gb-hero-subtitle">The most effective and time-tested weight loss surgery. Achieves <strong>~80% excess weight loss</strong> and resolves Type 2 Diabetes in most patients — performed laparoscopically or with robotic precision.</p>',
    new_html, flags=re.DOTALL
)
new_html = new_html.replace(
    'assets/img/gallbladder-hero-img.webp',
    'https://www.atulpeters.com/front/img/roux-en-img.png'
)
new_html = new_html.replace('alt="Laparoscopic Hernia Surgery Environment"', 'alt="Roux-en-Y Gastric Bypass"')

# Hero Stats
new_html = new_html.replace('<h4>25+ Years</h4>', '<h4>~80%</h4>')
new_html = new_html.replace('<p>Surgical Excellence</p>', '<p>Excess Weight Loss</p>')
new_html = new_html.replace('<h4>24 - 48 hours</h4>', '<h4>~85%</h4>')
new_html = new_html.replace('<p>Overnight Discharge</p>', '<p>T2 Diabetes Remission</p>')
new_html = new_html.replace('<h4>Critical View</h4>', '<h4>~45 Mins</h4>')
new_html = new_html.replace('<p>Sub-lay Mesh Placement</p>', '<p>Operating Time</p>')
new_html = new_html.replace('<h4>Cashless Facility</h4>', '<h4>1-2 Nights</h4>')
new_html = new_html.replace('<p>All Major Insurance Networks</p>', '<p>Hospital Stay</p>')

# Quick Nav
new_html = new_html.replace('<div class="gb-quick-nav-item"><a class="active" href="#symptoms">Hernia Overview</a></div>', '<div class="gb-quick-nav-item"><a class="active" href="#symptoms">Procedure Overview</a></div>')

# Overview section
new_html = new_html.replace('<span class="gb-section-tag">Anatomical Defect</span>', '<span class="gb-section-tag">Procedure Overview</span>')
new_html = new_html.replace('<h2 class="gb-section-title">Understanding Hernias &amp; Warning Signs</h2>', '<h2 class="gb-section-title">What is Roux-en-Y Gastric Bypass?</h2>')
new_html = re.sub(
    r'<p class="gb-section-desc">.*?</p>',
    '<p class="gb-section-desc">Roux-en-Y Gastric Bypass (RYGB) is a metabolic surgery with dual mechanisms: It works through <strong>restrictive changes</strong> (smaller stomach pouch) and, more importantly, <strong>metabolic changes</strong> (gut hormone reprogramming). Performed for over 60 years, RYGB is widely considered the <strong>"Gold Standard"</strong> in metabolic surgery.</p>',
    new_html, count=1, flags=re.DOTALL
)

# Replace the body of the symptoms creative grid with our RYGB body text and quick facts
# Using a simple string replace for the entire div
old_grid = re.search(r'(<div class="symptoms-creative-grid">.*?</div>\s*</div>\s*</section>)', new_html, flags=re.DOTALL)
if old_grid:
    new_grid = """<div class="gb-grid-2">
        <div class="gb-card">
          <h3>How Gastric Bypass Works</h3>
          <p>
            First, the surgeon creates a <strong>small stomach pouch</strong> — about the size of an egg (30–50 ml) —
            using surgical staplers, which immediately restricts the amount of food you can eat in a single sitting.
          </p>
          <p>
            Second, the small intestine is carefully divided and rerouted, bypassing <strong>100–170 cm</strong> of the
            upper intestine. Third, and most importantly for long-term success, the bypass reroutes food
            <strong>before</strong> it reaches the duodenum and proximal jejunum.
          </p>
          <div class="gb-highlight-box">
            <p>This dramatically alters gut hormone signaling — including <strong>GLP-1, PYY and ghrelin</strong> — to reduce hunger, enhance satiety, regulate blood sugar, and reset the body's weight set-point.</p>
          </div>
        </div>
        <div class="gb-card" style="background: linear-gradient(135deg, #0A1E30 0%, #154779 100%); color: #fff; border: none;">
            <h3 style="color: #fff;"><i class="fa-solid fa-list-check" style="color: #A8DECE;"></i> Quick Facts</h3>
            <ul class="gb-list" style="margin-top: 1rem;">
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>Excess Weight Loss:</strong> ~80%</li>
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>Diabetes Resolution:</strong> ~85%</li>
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>Hypertension Resolution:</strong> ~70%</li>
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>Cardiac Risk Reduction:</strong> ~60%</li>
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>PCOS Resolution:</strong> ~80%</li>
              <li style="color: #E2E8F0;"><i class="fa-solid fa-check" style="color: #A8DECE;"></i> <strong>Obstructive Sleep Apnoea:</strong> ~85%</li>
            </ul>
        </div>
      </div>
    </div>
  </section>"""
    new_html = new_html.replace(old_grid.group(1), new_grid)

# --- ADVANCED TECHNIQUES -> PROCEDURE STEPS ---
new_html = new_html.replace('<span class="gb-section-tag">Gold Standard Safety</span>', '<span class="gb-section-tag">The Procedure</span>')
new_html = new_html.replace('<h2 class="gb-section-title">The "Critical View of Safety" Technique</h2>', '<h2 class="gb-section-title">How Gastric Bypass Works</h2>')
new_html = new_html.replace('Dr. Peters strictly adheres to the internationally mandated <strong>Critical View of Safety (CVS)</strong> protocol. This ensures 100% anatomical clarity before any clipping or cutting, virtually eliminating the risk of accidental bile duct injury.', 'A precise, minimally invasive surgery that creates a new pathway for digestion and absorption. Performed via 4K Laparoscopic or Robotic approach.')

old_tech_grid = re.search(r'(<div class="gb-cvs-visual-grid">.*?</div>\s*</div>\s*</section>)', new_html, flags=re.DOTALL)
if old_tech_grid:
    new_tech = """<div class="gb-timeline-track" style="grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem;">
          <div class="gb-card">
            <h3><i class="fa-solid fa-user-check"></i> 1. Preparation</h3>
            <p>Comprehensive team evaluation. Thromboembolism prophylaxis is administered 12 hours before surgery.</p>
          </div>
          <div class="gb-card">
            <h3><i class="fa-solid fa-scissors"></i> 2. Incisions</h3>
            <p>3-4 small incisions (5-12mm) in the abdomen for camera and instruments. 5-6 ports for Robotic da Vinci.</p>
          </div>
          <div class="gb-card">
            <h3><i class="fa-solid fa-egg"></i> 3. The Pouch</h3>
            <p>A small gastric pouch (about 30-50ml) is created at the top of the stomach using staplers.</p>
          </div>
          <div class="gb-card">
            <h3><i class="fa-solid fa-route"></i> 4. The Bypass</h3>
            <p>The small intestine is divided, and 100-170 cm is bypassed. Lower intestine connects to the new pouch.</p>
          </div>
          <div class="gb-card">
            <h3><i class="fa-solid fa-link"></i> 5. Reconnection</h3>
            <p>The Y-shaped reconnection allows digestive juices to mix with food further down the intestine.</p>
          </div>
          <div class="gb-card">
            <h3><i class="fa-solid fa-bed-pulse"></i> 6. Recovery</h3>
            <p>Stand and walk within 4 hours. Clear liquids same evening. Discharged within 24-48 hours.</p>
          </div>
      </div>
    </div>
  </section>"""
    new_html = new_html.replace(old_tech_grid.group(1), new_tech)


# About section remains mostly unchanged, except we update the active nav script at the end
new_html = new_html.replace("var p = 'hernia-surgery-in-delhi.html';", "var p = 'roux-en-y-gastric-bypass.html';")

# Just do a rough rewrite of the rest to make it match the design.
with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
