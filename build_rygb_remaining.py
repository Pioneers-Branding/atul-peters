import re

with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'r', encoding='utf-8') as f:
    html = f.read()

# --- RECOVERY TIMELINE (Journey) ---
html = html.replace('Your 24-Hour Hernia Surgery Journey', 'Your Typical Weight Loss Journey')
html = html.replace('We combine Enhanced Recovery After Surgery (ERAS) pathways with compassionate hospital care to ensure your hernia repair is swift, painless, and completely stress-free.', 'Most patients experience rapid weight loss in the first 6 months, followed by steady progress towards their goal over 18 to 24 months.')
html = html.replace('<span class="gb-section-tag">Seamless Recovery</span>', '<span class="gb-section-tag">Expected Outcomes</span>')

old_journey_grid = re.search(r'(<div class="gb-journey-grid">.*?</div>\s*</div>\s*</section>)', html, flags=re.DOTALL)
if old_journey_grid:
    new_journey = """<div class="gb-journey-grid">
        <div class="gb-journey-card">
          <div class="gb-j-icon"><i class="fa-solid fa-arrow-trend-down"></i></div>
          <div class="gb-j-time">1 Month</div>
          <div class="gb-j-title">Rapid Initial Loss</div>
          <p class="gb-j-desc">~15% excess weight loss.</p>
        </div>
        <div class="gb-journey-card">
          <div class="gb-j-icon"><i class="fa-solid fa-person-running"></i></div>
          <div class="gb-j-time">3 Months</div>
          <div class="gb-j-title">Increased Energy</div>
          <p class="gb-j-desc">~30% excess weight loss.</p>
        </div>
        <div class="gb-journey-card">
          <div class="gb-j-icon"><i class="fa-solid fa-scale-balanced"></i></div>
          <div class="gb-j-time">6 Months</div>
          <div class="gb-j-title">Halfway to Goal</div>
          <p class="gb-j-desc">~50% excess weight loss.</p>
        </div>
        <div class="gb-journey-card">
          <div class="gb-j-icon"><i class="fa-solid fa-heart-pulse"></i></div>
          <div class="gb-j-time">12 Months</div>
          <div class="gb-j-title">Major Transformation</div>
          <p class="gb-j-desc">~70% excess weight loss.</p>
        </div>
        <div class="gb-journey-card">
          <div class="gb-j-icon"><i class="fa-solid fa-trophy"></i></div>
          <div class="gb-j-time">18-24 Months</div>
          <div class="gb-j-title">Maximum Loss</div>
          <p class="gb-j-desc">~80% excess weight loss.</p>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_journey_grid.group(1), new_journey)

# --- DIET ---
html = html.replace('Life After Hernia Surgery: What to Eat &amp; Activities', 'Post-Surgery Diet: Phase I')
html = html.replace('After hernia reconstruction, most patients can resume their diet fairly quickly. There are generally no specific long-term dietary restrictions imposed by the surgery itself.', 'The first step in your recovery is a structured clear liquid phase. Here are the essential Do\'s and Don\'ts.')

old_diet_grid = re.search(r'(<div class="diet-modern-grid">.*?</div>\s*</div>\s*</section>)', html, flags=re.DOTALL)
if old_diet_grid:
    new_diet = """<div class="diet-modern-grid">
        <div class="diet-modern-card diet-modern-card--success">
          <i class="fa-solid fa-circle-check diet-modern-icon"></i>
          <h3>✓ Do's</h3>
          <p>
            • Non-aerated, clear liquids<br/>
            • Sip slowly throughout the day (50 to 100ml every hour)<br/>
            • Aim for 2 to 2.5L per day<br/>
            • Stop immediately if you feel full, pain or discomfort
          </p>
        </div>
        <div class="diet-modern-card diet-modern-card--alert">
          <i class="fa-solid fa-circle-xmark diet-modern-icon"></i>
          <h3>✗ Don'ts</h3>
          <p>
            • Avoid sweetened beverages (calories + dumping syndrome risk)<br/>
            • No carbonated beverages (can stretch the pouch)<br/>
            • No alcoholic drinks (absorbed faster, higher intoxication)<br/>
            • Never use straws (introduces air, causes discomfort)
          </p>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_diet_grid.group(1), new_diet)

# --- COST ---
html = html.replace('Hernia Surgery Cost', 'RYGB Cost in Delhi')
old_cost_card = re.search(r'(<div class="finance-card">.*?</div>)', html, flags=re.DOTALL)
if old_cost_card:
    new_cost_card = """<div class="finance-card">
          <div class="finance-icon"><i class="fa-solid fa-indian-rupee-sign"></i></div>
          <h3>Transparent Pricing</h3>
          <ul class="gb-list" style="margin-top: 1.5rem; color: #4a5568;">
            <li><i class="fa-solid fa-check" style="color:#38a169;"></i> Surgeon + Anaesthesia Included</li>
            <li><i class="fa-solid fa-check" style="color:#38a169;"></i> OT &amp; 1–2 nights stay Included</li>
            <li><i class="fa-solid fa-check" style="color:#38a169;"></i> 1-year dietitian follow-up Included</li>
            <li><i class="fa-solid fa-check" style="color:#38a169;"></i> Robotic (da Vinci) upgrade as Add-on</li>
          </ul>
        </div>"""
    html = html.replace(old_cost_card.group(1), new_cost_card)

old_insurance_card = re.search(r'(<div class="finance-card">.*?<h3>Health Insurance &amp; EMI</h3>.*?</div>)', html, flags=re.DOTALL)
if old_insurance_card:
    new_insurance_card = """<div class="finance-card">
          <div class="finance-icon" style="background:#fff5f5;color:#e53e3e;"><i class="fa-solid fa-shield-halved"></i></div>
          <h3>Insurance &amp; Financing</h3>
          <ul class="gb-list" style="margin-top: 1.5rem; color: #4a5568;">
            <li><i class="fa-solid fa-check" style="color:#e53e3e;"></i> IRDA-approved bariatric cover</li>
            <li><i class="fa-solid fa-check" style="color:#e53e3e;"></i> Cashless network (Max, MediAssist)</li>
            <li><i class="fa-solid fa-check" style="color:#e53e3e;"></i> EMI options (0% on select cards)</li>
            <li><i class="fa-solid fa-check" style="color:#e53e3e;"></i> Approx. self-pay range: INR 4.5L – 6.5L</li>
          </ul>
        </div>"""
    html = html.replace(old_insurance_card.group(1), new_insurance_card)

# --- FAQS ---
html = html.replace('Hernia Surgery Questions', 'RYGB Questions')
old_faqs = re.search(r'(<div class="gb-faq-list">.*?</div>\s*</div>\s*</section>)', html, flags=re.DOTALL)
if old_faqs:
    new_faqs = """<div class="gb-faq-list">
        <div class="gb-faq-item active">
          <button class="gb-faq-question">
            What exactly is done during a Roux-en-Y Gastric Bypass?
            <i class="fa-solid fa-chevron-down"></i>
          </button>
          <div class="gb-faq-answer" style="max-height: 500px;">
            <p>The surgeon creates a small (30 ml) egg-sized stomach pouch and reroutes the small intestine to bypass 100–170 cm of the upper gut, forming the Y-shaped reconnection. It is performed laparoscopically or with the da Vinci robot through 3–6 small incisions. Operative time is typically 45-90 minutes and hospital stay is 1-2 nights.</p>
          </div>
        </div>
        <div class="gb-faq-item">
          <button class="gb-faq-question">
            How is RYGB different from sleeve gastrectomy and mini gastric bypass?
            <i class="fa-solid fa-chevron-down"></i>
          </button>
          <div class="gb-faq-answer">
            <p>RYGB combines restriction with metabolic hormone reprogramming, giving the highest diabetes remission (~85%) and reliable reflux improvement. Sleeve gastrectomy removes ~75% of the stomach but is irreversible. Mini gastric bypass has a simpler single-loop anatomy but slightly less long-term data.</p>
          </div>
        </div>
        <div class="gb-faq-item">
          <button class="gb-faq-question">
            What is the BMI requirement for gastric bypass in India?
            <i class="fa-solid fa-chevron-down"></i>
          </button>
          <div class="gb-faq-answer">
            <p>In India, RYGB is recommended for BMI ≥ 35 kg/m² with or without comorbidities, or BMI ≥ 32.5 kg/m² with Type 2 Diabetes or other obesity-related conditions. For Asian patients these thresholds may be lowered by 2.5 points per IFSO-Asia guidelines.</p>
          </div>
        </div>
        <div class="gb-faq-item">
          <button class="gb-faq-question">
            Can I have RYGB if I have Type 2 Diabetes?
            <i class="fa-solid fa-chevron-down"></i>
          </button>
          <div class="gb-faq-answer">
            <p>Yes — Type 2 Diabetes is the single strongest indication for RYGB. Studies show ~85% remission rates, often within days of surgery, independent of weight loss, due to changes in gut hormones GLP-1, PYY and ghrelin.</p>
          </div>
        </div>
        <div class="gb-faq-item">
          <button class="gb-faq-question">
            Will I regain weight after gastric bypass surgery?
            <i class="fa-solid fa-chevron-down"></i>
          </button>
          <div class="gb-faq-answer">
            <p>Most patients maintain 70–80% of their excess weight loss at 10 years. Weight regain of 5–10% can occur around 18–24 months if dietary and exercise guidelines are not followed. Long-term success depends on adherence to follow-up, protein intake and physical activity.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_faqs.group(1), new_faqs)

# --- APPOINTMENT SECTION ---
html = html.replace('Ready to Learn if <span class="appt-title-accent">Hernia Surgery</span><br />is Right for You?', 'Ready to Learn if <span class="appt-title-accent">Gastric Bypass</span><br />is Right for You?')
html = html.replace('id="gbAppointmentForm"', 'id="rygbAppointmentForm"')
html = html.replace('<option selected="" value="hernia">Hernia Surgery</option>', '<option selected="" value="rygb">Roux-en-Y Gastric Bypass</option>')

with open(r'e:\atul-peters\atul-peters\roux-en-y-gastric-bypass.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Remaining replacements applied successfully.")
