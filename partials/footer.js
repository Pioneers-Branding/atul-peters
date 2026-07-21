var basePath = '';
if (window.location.pathname.indexOf('/weight-loss-surgery/') !== -1 || window.location.pathname.indexOf('/surgery-for-diabetes/') !== -1) {
  basePath = '../';
}

document.write(`<!-- ============================================
   SITE FOOTER (Partial)
   Edit this file to update footer on ALL pages
   ============================================ -->

<footer class="footer" id="contact">
  <div class="footer-bg-glow" aria-hidden="true"></div>
  <div class="container">

    <!-- Centered big logo + tagline -->
    <div class="footer-hero">
      <a href="${basePath}index.html" class="footer-logo-big" aria-label="Dr. Atul Peters - Home">
        <img src="https://www.atulpeters.com/front/img/logo-04.png" alt="Dr. Atul Peters" class="footer-logo-img"
          onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 200 60%22%3E%3Ctext x=%22100%22 y=%2240%22 text-anchor=%22middle%22 font-family=%22Georgia%22 font-size=%2230%22 fill=%22%23fff%22%3EDr. Atul Peters%3C/text%3E%3C/svg%3E'">
      </a>
      <div class="footer-tagline-wrap">
        <p class="footer-tagline">Compassionate surgical care, advanced bariatric, metabolic, robotic &amp; general surgical solutions, and lifelong wellness — guiding patients across India and beyond for over 25 years.
        </p>
      </div>
      <div class="footer-social">
        <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
          </svg></a>
        <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="2" y="2" width="20" height="20" rx="5" />
            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
          </svg></a>
        <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.4 19.6c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z" />
            <polygon points="9.75 15.02 15.5 12 9.75 8.48 9.75 15.02" fill="#fff" />
          </svg></a>
        <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
            <rect x="2" y="9" width="4" height="12" />
            <circle cx="4" cy="4" r="2" />
          </svg></a>
        <a href="#" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884" />
          </svg></a>
      </div>
    </div>

    <!-- Services columns -->
    <div class="footer-services">
      <div class="footer-col">
        <h4>Bariatric &amp; Metabolic</h4>
        <ul class="footer-links">
          <li><a href="${basePath}roux-en-y-gastric-bypass.html"><span class="footer-link-dot"></span>Gastric Bypass</a></li>
          <li><a href="${basePath}weight-loss-surgery/sleeve-gastrectomy.html"><span class="footer-link-dot"></span>Sleeve Gastrectomy</a></li>
          <li><a href="${basePath}weight-loss-surgery/mini-gastric-bypass.html"><span class="footer-link-dot"></span>Mini Gastric Bypass</a></li>
          <li><a href="${basePath}surgery-for-diabetes/overview.html"><span class="footer-link-dot"></span>Surgery for Diabetes</a></li>
          <li><a href="${basePath}weight-loss-surgery-in-delhi.html"><span class="footer-link-dot"></span>WLS in Delhi NCR</a></li>
          <li><a href="${basePath}weight-loss-surgery/other-laparoscopic-procedures.html"><span class="footer-link-dot"></span>Revision Surgery</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>General &amp; Robotic</h4>
        <ul class="footer-links">
          <li><a href="${basePath}other-surgeries/robotic-surgery.html"><span class="footer-link-dot"></span>Robotic Surgery</a></li>
          <li><a href="${basePath}other-surgeries/laparoscopic-cholecystectomy.html"><span class="footer-link-dot"></span>Gallbladder Surgery</a></li>
          <li><a href="${basePath}other-surgeries/laparoscopic-hernioplasty-ventral-inguinal.html"><span class="footer-link-dot"></span>Hernia Repair (eTEP/TAR)</a></li>
          <li><a href="${basePath}other-surgeries/fundoplication-for-gastro-esophageal-reflux-disease.html"><span class="footer-link-dot"></span>GERD &amp; Reflux Surgery</a></li>
          <li><a href="${basePath}other-surgeries/laparoscopic-appendicectomy.html"><span class="footer-link-dot"></span>Appendix Surgery</a></li>
          <li><a href="${basePath}other-surgeries/piles-hemorrhoids.html"><span class="footer-link-dot"></span>Laser Piles Surgery (LHP)</a></li>
          <li><a href="${basePath}other-surgeries/rectal-prolapse.html"><span class="footer-link-dot"></span>Rectal Prolapse (LVMR)</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Delhi NCR Services</h4>
        <ul class="footer-links">
          <li><a href="${basePath}weight-loss-surgery-in-delhi.html"><span class="footer-link-dot"></span>Weight Loss Surgery</a></li>
          <li><a href="${basePath}hernia-surgery-in-delhi.html"><span class="footer-link-dot"></span>Hernia Surgery</a></li>
          <li><a href="${basePath}laparoscopic-surgery-in-delhi.html"><span class="footer-link-dot"></span>Laparoscopic Surgery</a></li>
          <li><a href="${basePath}robotic-surgery-in-delhi.html"><span class="footer-link-dot"></span>Robotic Surgery</a></li>
          <li><a href="${basePath}best-appendix-surgery-in-delhi-india.html"><span class="footer-link-dot"></span>Appendix Surgery</a></li>
          <li><a href="${basePath}best-gallbladder-surgery-in-delhi.html"><span class="footer-link-dot"></span>Gallbladder Surgery</a></li>
          <li><a href="${basePath}east-delhi.html"><span class="footer-link-dot"></span>East Delhi Clinic</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="${basePath}about.html"><span class="footer-link-dot"></span>About Dr. Peters</a></li>
          <li><a href="${basePath}workshop-conferences.html"><span class="footer-link-dot"></span>Workshops &amp; Conferences</a></li>
          <li><a href="${basePath}events.html"><span class="footer-link-dot"></span>Events &amp; Workshops</a></li>
          <li><a href="${basePath}publications.html"><span class="footer-link-dot"></span>Publications</a></li>
          <li><a href="${basePath}weight-loss.html#success"><span class="footer-link-dot"></span>Success Stories</a></li>
          <li><a href="${basePath}fitness-factory.html"><span class="footer-link-dot"></span>Peter's Fitness Factory</a></li>
          <li><a href="${basePath}smart-weight-loss.html"><span class="footer-link-dot"></span>Smart Weight Loss</a></li>
          <li><a href="${basePath}weight-loss.html#faq"><span class="footer-link-dot"></span>FAQ</a></li>
          <li><a href="${basePath}contact.html"><span class="footer-link-dot"></span>Book Consultation</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Get in Touch</h4>
        <div class="footer-contact">
          <a href="tel:+917770001900" class="footer-contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path
                d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 0 2 1.72" />
            </svg>
            <div><strong>+91-7770001900</strong><span>Mon–Sat · 9am – 7pm(IST)</span></div>
          </a>
          <a href="mailto:info@atulpeters.com" class="footer-contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
              <polyline points="22,6 12,13 2,6" />
            </svg>
            <div><strong>info@atulpeters.com</strong><span>We reply within 24 hours</span></div>
          </a>
          <div class="footer-contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
              <circle cx="12" cy="10" r="3" />
            </svg>
            <div><strong>Max Smart Super Speciality Hospital, Saket, </strong><span>New Delhi - 110017, India</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; 2026 Dr. Atul Peters. All rights reserved.</p>
      <div class="footer-legal">
        <a href="${basePath}privacy-policy.html">Privacy Policy</a>
        <a href="${basePath}disclaimer.html">Terms of Service</a>
        <a href="${basePath}index.html">Sitemap</a>
      </div>
    </div>
  </div>
</footer>`);