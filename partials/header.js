var basePath = '';
if (window.location.pathname.indexOf('/weight-loss-surgery/') !== -1 || window.location.pathname.indexOf('/surgery-for-diabetes/') !== -1) {
  basePath = '../';
}

document.write(`<!-- ============================================
   SITE HEADER (Partial)
   Edit this file to update header on ALL pages
   ============================================ -->

<!-- Top Bar -->
<div class="top-bar">
  <div class="top-bar-inner">
    <div class="top-bar-left">
      <span class="top-bar-badge">Limca Book Record Holder</span>
      <span class="top-bar-divider">|</span>
      <a href="tel:+917770001900" class="top-bar-phone">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path
            d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 0 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
        </svg>
        +91-7770001900
      </a>
      <a href="tel:+911139595519" class="top-bar-phone">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path
            d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 0 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
        </svg>
        +91-11-39595119
      </a>
    </div>
    <div class="top-bar-right">
      <a href="https://www.facebook.com/dratulpeters" target="_blank" class="top-social" aria-label="Facebook">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
          <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
        </svg>
      </a>
      <a href="https://www.instagram.com/dratulpeters/" target="_blank" class="top-social" aria-label="Instagram">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="2" y="2" width="20" height="20" rx="5" />
          <circle cx="12" cy="12" r="4" />
          <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" />
        </svg>
      </a>
      <a href="https://www.youtube.com/user/chrysalishealthcare" target="_blank" class="top-social"
        aria-label="YouTube">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
          <path
            d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.4 19.6c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z" />
          <polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white" />
        </svg>
      </a>
      <a href="https://in.linkedin.com/in/dr-atul-n-c-peters-6a854444" target="_blank" class="top-social"
        aria-label="LinkedIn">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
          <rect x="2" y="9" width="4" height="12" />
          <circle cx="4" cy="4" r="2" />
        </svg>
      </a>
      <span class="top-bar-divider">|</span>
      <a href="${basePath}travel-desk.html" class="top-bar-link">Travel Desk</a>
    </div>
  </div>
</div>

<!-- Navigation -->
<nav class="navbar" id="navbar">
  <div class="nav-inner">
    <a href="${basePath}index.html" class="nav-logo">
      <img src="https://www.atulpeters.com/front/img/logo-04.png" alt="Dr. Atul Peters" class="logo-img"
        onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ccircle cx=%2250%22 cy=%2250%22 r=%2245%22 fill=%22%23B8975A%22/%3E%3Ctext x=%2250%22 y=%2258%22 font-size=%2238%22 fill=%22white%22 text-anchor=%22middle%22%3EAP%3C/text%3E%3C/svg%3E'">
    </a>

    <ul class="nav-menu" id="navLinks">
      <li class="nav-item"><a href="${basePath}about.html" class="nav-link">About</a></li>

      <!-- ==================== WEIGHT LOSS SURGERY ==================== -->
      <li class="nav-item has-mega">
        <a href="${basePath}weight-loss-surgery/overview.html" class="nav-link" data-page="weight-loss">
          Weight Loss Surgery
          <svg class="nav-link-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </a>
        <div class="mega-menu">
          <div class="mega-menu-inner">
            <div class="mega-menu-grid">
              <div class="mega-menu-col">
                <span class="mega-menu-label">Procedures</span>
                <a href="${basePath}roux-en-y-gastric-bypass.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Roux-en-Y Gastric Bypass</strong>
                    <small>Gold-standard bypass with proven long-term results</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/sleeve-gastrectomy.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Sleeve Gastrectomy</strong>
                    <small>Most common weight loss procedure worldwide</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/mini-gastric-bypass.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Mini Gastric Bypass</strong>
                    <small>Simpler, shorter surgery with similar outcomes</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/banded-bariatric-procedures.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Banded Bariatric Procedures</strong>
                    <small>Adjustable band added to other surgeries</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/gastric-banding.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-ring"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Gastric Banding (LAGB)</strong>
                    <small>Reversible adjustable silicone band</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/intra-gastric-balloon.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Intra Gastric Balloon</strong>
                    <small>Non-surgical, temporary weight loss option</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/other-laparoscopic-procedures.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-user-md"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>GI &amp; MAS Surgeries</strong>
                    <small>Hernia, gallbladder &amp; reflux repair</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-col">
                <span class="mega-menu-label">Learn More</span>
                <a href="${basePath}weight-loss-surgery/overview.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-book-open"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Overview</strong>
                    <small>Introduction to bariatric &amp; metabolic surgery</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/candidate.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-user-check"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Are You a Candidate?</strong>
                    <small>BMI criteria, eligibility, and indications</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/faqs.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-question"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>FAQs</strong>
                    <small>30+ questions answered by Dr. Peters</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-feature">
                <div class="mega-menu-feature-inner">
                  <span class="mega-menu-feature-eyebrow">Limca Book Record</span>
                  <h4>5,000+ Bariatric<br>Surgeries Performed</h4>
                  <p>India's most experienced bariatric surgeon with outcomes that match the best centers in the world.</p>
                  <a href="${basePath}contact.html" class="mega-menu-feature-cta">
                    Book a Consultation
                    <i class="fa-solid fa-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>

      <!-- ==================== SURGERY FOR DIABETES ==================== -->
      <li class="nav-item has-mega">
        <a href="${basePath}surgery-for-diabetes/overview.html" class="nav-link">
          Surgery for Diabetes
          <svg class="nav-link-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </a>
        <div class="mega-menu">
          <div class="mega-menu-inner">
            <div class="mega-menu-grid">
              <div class="mega-menu-col">
                <span class="mega-menu-label">Metabolic Procedures</span>
                <a href="${basePath}surgery-for-diabetes/overview.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Overview</strong>
                    <small>How surgery can reverse Type 2 Diabetes</small>
                  </span>
                </a>
                <a href="${basePath}surgery-for-diabetes/laparoscopic-ileal-interposition.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Laparoscopic Ileal Interposition</strong>
                    <small>Repositioning intestinal segments for hormonal reset</small>
                  </span>
                </a>
                <a href="${basePath}surgery-for-diabetes/laparoscopic-duodenojejunal-bypass.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Duodenojejunal Bypass</strong>
                    <small>Bypass first portion of small intestine</small>
                  </span>
                </a>
                <a href="${basePath}surgery-for-diabetes/sleeve-gastrectomy-with-proximal-jejunal-bypass.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-dot"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Sleeve with Proximal Jejunal Bypass</strong>
                    <small>Combined sleeve and metabolic bypass</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-col">
                <span class="mega-menu-label">Patient Resources</span>
                <a href="${basePath}weight-loss-surgery/candidate.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-clipboard-check"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Eligibility &amp; Indications</strong>
                    <small>Who qualifies for metabolic surgery</small>
                  </span>
                </a>
                <a href="${basePath}about.html#publications" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-vial"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Outcomes &amp; Research</strong>
                    <small>Long-term diabetes remission data</small>
                  </span>
                </a>
                <a href="${basePath}weight-loss-surgery/faqs.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-question"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>FAQs</strong>
                    <small>Answers about diabetes surgery</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-feature mega-menu-feature--alt">
                <div class="mega-menu-feature-inner">
                  <span class="mega-menu-feature-eyebrow">Diabetes Reversal</span>
                  <h4>80% Patients Off<br>Insulin in 1 Year</h4>
                  <p>Metabolic surgery delivers long-term Type 2 Diabetes remission — often within days of the procedure.</p>
                  <a href="${basePath}contact.html" class="mega-menu-feature-cta">
                    Check Eligibility
                    <i class="fa-solid fa-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="nav-item"><a href="${basePath}other-surgeries/robotic-surgery.html" class="nav-link">Robotic Surgery</a></li>
      <li class="nav-item has-dropdown">
        <a href="${basePath}weight-loss-surgery/other-laparoscopic-procedures.html" class="nav-link">
          GI &amp; MAS
          <svg class="nav-link-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </a>
        <div class="dropdown">
          <a href="${basePath}weight-loss-surgery/other-laparoscopic-procedures.html" class="dropdown-item">Overview</a>
          <a href="${basePath}other-surgeries/laparoscopic-cholecystectomy.html" class="dropdown-item">Laparoscopic Cholecystectomy</a>
          <a href="${basePath}other-surgeries/laparoscopic-hernioplasty-ventral-inguinal.html" class="dropdown-item">Laparoscopic Hernioplasty (eTEP/TAR)</a>
          <a href="${basePath}other-surgeries/fundoplication-for-gastro-esophageal-reflux-disease.html" class="dropdown-item">Fundoplication for GERD</a>
          <a href="${basePath}other-surgeries/laparoscopic-appendicectomy.html" class="dropdown-item">Laparoscopic Appendicectomy</a>
          <a href="${basePath}other-surgeries/laser-fistulectomy.html" class="dropdown-item">Laser Proctology (FiLaC)</a>
          <a href="${basePath}other-surgeries/piles-hemorrhoids.html" class="dropdown-item">Piles &amp; Hemorrhoids (Laser/MIPH)</a>
          <a href="${basePath}other-surgeries/rectal-prolapse.html" class="dropdown-item">Laparoscopic Rectal Prolapse</a>
        </div>
      </li>

      <!-- ==================== SMART NUTRITION ==================== -->
      <li class="nav-item has-mega">
        <a href="${basePath}nutrition-clinic.html" class="nav-link">
          Smart Nutrition
          <svg class="nav-link-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </a>
        <div class="mega-menu">
          <div class="mega-menu-inner">
            <div class="mega-menu-grid">
              <div class="mega-menu-col">
                <span class="mega-menu-label">Nutrition Services</span>
                <a href="${basePath}nutrition-clinic.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-apple-whole"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Nutrition Clinic</strong>
                    <small>Personalized diet plans by certified dietitians</small>
                  </span>
                </a>
                <a href="${basePath}smart-weight-loss.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-weight-scale"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Smart Weight Loss</strong>
                    <small>Medically supervised, non-surgical program</small>
                  </span>
                </a>
                <a href="${basePath}fitness-factory.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-dumbbell"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Peter's Fitness Factory</strong>
                    <small>Bariatric rehab &amp; metabolic strength center</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-col">
                <span class="mega-menu-label">Tools &amp; Guides</span>
                <a href="${basePath}bmi-calculator.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-calculator"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>BMI Calculator</strong>
                    <small>Calculate your body mass index instantly</small>
                  </span>
                </a>
                <a href="${basePath}nutrition-clinic.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-utensils"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Diet Plans</strong>
                    <small>Pre-op and post-op meal plans</small>
                  </span>
                </a>
                <a href="${basePath}blog.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-newspaper"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Nutrition Blog</strong>
                    <small>Expert articles on healthy eating</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-feature">
                <div class="mega-menu-feature-inner">
                  <span class="mega-menu-feature-eyebrow">Personalized Plans</span>
                  <h4>Tailored to Your<br>Goals &amp; Lifestyle</h4>
                  <p>Our dietitians create custom plans that work with your surgery, schedule, and food preferences.</p>
                  <a href="${basePath}contact.html" class="mega-menu-feature-cta">
                    Book a Dietitian
                    <i class="fa-solid fa-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>

      <!-- ==================== SUCCESS STORIES ==================== -->
      <li class="nav-item has-mega">
        <a href="${basePath}weight-loss.html#success" class="nav-link">
          Success Stories
          <svg class="nav-link-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </a>
        <div class="mega-menu">
          <div class="mega-menu-inner">
            <div class="mega-menu-grid">
              <div class="mega-menu-col">
                <span class="mega-menu-label">Patient Stories</span>
                <a href="${basePath}weight-loss.html#success" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-images"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Before &amp; After Pictures</strong>
                    <small>Real patient transformations gallery</small>
                  </span>
                </a>
                <a href="${basePath}about.html#videos" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-circle-play"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Video Testimonials</strong>
                    <small>Hear directly from our patients</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-col">
                <span class="mega-menu-label">Resources</span>
                <a href="${basePath}blog.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-newspaper"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>News &amp; Articles</strong>
                    <small>Latest updates from the clinic</small>
                  </span>
                </a>
                <a href="${basePath}events.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-regular fa-calendar"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Events &amp; Workshops</strong>
                    <small>Upcoming seminars and live workshops</small>
                  </span>
                </a>
                <a href="${basePath}workshop-conferences.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-chalkboard-user"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Workshops &amp; Conferences</strong>
                    <small>Scientific congresses &amp; faculty archive</small>
                  </span>
                </a>
                <a href="${basePath}publications.html" class="mega-menu-item">
                  <span class="mega-menu-item-icon"><i class="fa-solid fa-book"></i></span>
                  <span class="mega-menu-item-text">
                    <strong>Publications</strong>
                    <small>Dr. Peters' research &amp; papers</small>
                  </span>
                </a>
              </div>

              <div class="mega-menu-feature mega-menu-feature--alt">
                <div class="mega-menu-feature-inner">
                  <span class="mega-menu-feature-eyebrow">Real Patients</span>
                  <h4>50 kg Lost.<br>Life Regained.</h4>
                  <p>Browse inspiring journeys of patients who transformed their health and confidence.</p>
                  <a href="${basePath}weight-loss.html#success" class="mega-menu-feature-cta">
                    View All Stories
                    <i class="fa-solid fa-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>     
    </ul>

    <div class="nav-actions">
      <a href="${basePath}contact.html" class="nav-cta">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="4" width="18" height="18" rx="2" />
          <line x1="16" y1="2" x2="16" y2="6" />
          <line x1="8" y1="2" x2="8" y2="6" />
          <line x1="3" y1="10" x2="21" y2="10" />
        </svg>
        Book Appointment
      </a>
    </div>

    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>`);