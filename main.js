/* ===================================
   Dr. Atul Peters - JavaScript
   Premium Clinical Design v1.0
   =================================== */



function setActiveNavLink() {
  const p = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar .nav-link').forEach(function(l) {
    const href = (l.getAttribute('href') || '').split('#')[0];
    if (href === p) l.classList.add('nav-link--active');
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setActiveNavLink();

  initNavigation();
  initScrollAnimations();
  initFAQAccordion();
  initBMICalculator();
  initCounters();
  initSmoothScroll();
  initFormHandler();
  initStickyNav();
  initBackToTop();
  initJourneySpine();
  initHeroVideo();
  initSuccessCarousel();
  initVideoList();
  initFitnessFactory();
});

/* === Navigation === */
function initNavigation() {
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  navToggle?.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = navLinks.classList.toggle('open');
    navToggle.classList.toggle('open', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target)) {
      navLinks.classList.remove('open');
      navToggle.classList.remove('open');
      document.body.style.overflow = '';
    }
  });

  navLinks?.querySelectorAll('.nav-item.has-dropdown > .nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
      if (window.innerWidth <= 992) {
        e.preventDefault();
        const navItem = link.parentElement;
        navLinks.querySelectorAll('.nav-item.has-dropdown').forEach(item => {
          if (item !== navItem) item.classList.remove('active');
        });
        navItem.classList.toggle('active');
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      navLinks?.classList.remove('open');
      navToggle?.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}

/* === Sticky Nav === */
function initStickyNav() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* === Smooth Scroll === */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        const navHeight = document.getElementById('navbar')?.offsetHeight || 64;
        const top = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 20;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });
}

/* === Scroll Animations === */
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  const cards = document.querySelectorAll('.focus-card, .treatment-card, .blog-card, .edu-card, .hero-card, .int-service');
  cards.forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 0.5s ease ${i * 0.06}s, transform 0.5s ease ${i * 0.06}s`;
    observer.observe(card);
  });
}

/* === FAQ Accordion === */
function initFAQAccordion() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const question = item.querySelector('.faq-question');
    if (!question) return;
    const setExpanded = (open) => {
      question.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      document.querySelectorAll('.faq-item').forEach(other => {
        if (other !== item) {
          other.classList.remove('active');
          const q = other.querySelector('.faq-question');
          q?.setAttribute('aria-expanded', 'false');
        }
      });
      const willOpen = !isActive;
      item.classList.toggle('active', willOpen);
      setExpanded(willOpen);
    });
    question.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        question.click();
      }
    });
  });
}

/* === BMI Calculator === */
function initBMICalculator() {
  const heightInput = document.getElementById('height');
  const weightInput = document.getElementById('weight');
  const heightValue = document.getElementById('heightValue');
  const weightValue = document.getElementById('weightValue');
  const bmiNumber = document.getElementById('bmiNumber');
  const bmiCategory = document.getElementById('bmiCategory');
  const bmiAdvice = document.getElementById('bmiAdvice');
  const bmiNeedle = document.getElementById('bmiNeedle');
  const bmiGaugeArc = document.getElementById('bmiGaugeArc');

  if (!heightInput || !weightInput) return;

  // Gauge arc: half-circle path, length is ~251
  const ARC_LEN = 251;

  const CATS_CAUCASIAN = [
    { max: 18.5, cat: 'Underweight',    numColor: '#60A5FA', bg: 'rgba(96,165,250,0.18)',  border: 'rgba(96,165,250,0.4)',  adv: 'You may need to gain weight. Consult with a nutritionist.' },
    { max: 25,   cat: 'Normal Weight',  numColor: '#34D399', bg: 'rgba(52,211,153,0.18)',  border: 'rgba(52,211,153,0.4)',  adv: 'Great! Maintain your healthy weight with balanced diet.' },
    { max: 30,   cat: 'Overweight',     numColor: '#FBBF24', bg: 'rgba(251,191,36,0.18)',  border: 'rgba(251,191,36,0.4)',  adv: 'Consider lifestyle changes. A consultation can help.' },
    { max: 35,   cat: 'Class I Obesity',numColor: '#FB923C', bg: 'rgba(251,146,60,0.18)',  border: 'rgba(251,146,60,0.4)',  adv: 'You may be a candidate for bariatric surgery.' },
    { max: 40,   cat: 'Class II Obesity',numColor: '#F97316',bg: 'rgba(249,115,22,0.20)',  border: 'rgba(249,115,22,0.45)', adv: 'Bariatric surgery could significantly improve your health.' },
    { max: 999,  cat: 'Class III Obesity',numColor: '#EF4444', bg: 'rgba(239,68,68,0.20)',  border: 'rgba(239,68,68,0.45)',  adv: 'We strongly recommend scheduling a consultation.' }
  ];

  const CATS_ASIAN = [
    { max: 18.5, cat: 'Underweight',    numColor: '#60A5FA', bg: 'rgba(96,165,250,0.18)',  border: 'rgba(96,165,250,0.4)',  adv: 'You may need to gain weight. Consult with a nutritionist.' },
    { max: 23,   cat: 'Normal Weight',  numColor: '#34D399', bg: 'rgba(52,211,153,0.18)',  border: 'rgba(52,211,153,0.4)',  adv: 'Great! Maintain your healthy weight with balanced diet.' },
    { max: 25,   cat: 'Overweight',     numColor: '#FBBF24', bg: 'rgba(251,191,36,0.18)',  border: 'rgba(251,191,36,0.4)',  adv: 'Consider lifestyle changes. A consultation can help.' },
    { max: 30,   cat: 'Class I Obesity',numColor: '#FB923C', bg: 'rgba(251,146,60,0.18)',  border: 'rgba(251,146,60,0.4)',  adv: 'You may be a candidate for bariatric surgery.' },
    { max: 35,   cat: 'Class II Obesity',numColor: '#F97316',bg: 'rgba(249,115,22,0.20)',  border: 'rgba(249,115,22,0.45)', adv: 'Bariatric surgery could significantly improve your health.' },
    { max: 999,  cat: 'Class III Obesity',numColor: '#EF4444', bg: 'rgba(239,68,68,0.20)',  border: 'rgba(239,68,68,0.45)',  adv: 'We strongly recommend scheduling a consultation.' }
  ];

  function getCat(bmi) {
    const ethnicity = document.querySelector('input[name="ethnicity"]:checked')?.value || 'caucasian';
    const CATS = ethnicity === 'asian' ? CATS_ASIAN : CATS_CAUCASIAN;
    return CATS.find(c => bmi < c.max) || CATS[CATS.length - 1];
  }

  // Update slider gradient fill
  function updateSliderFill(input) {
    const min = +input.min, max = +input.max, val = +input.value;
    const pct = ((val - min) / (max - min)) * 100;
    input.parentElement.style.setProperty('--pct', pct + '%');
  }

  function calculateBMI() {
    const h = parseInt(heightInput.value);
    const w = parseInt(weightInput.value);
    if (!h || !w) return;

    heightValue.textContent = `${h} cm`;
    weightValue.textContent = `${w} kg`;

    const bmi = w / ((h / 100) ** 2);
    bmiNumber.textContent = bmi.toFixed(1);

    const c = getCat(bmi);
    bmiNumber.style.color = c.numColor;
    bmiCategory.textContent = c.cat;
    bmiCategory.style.background = c.bg;
    bmiCategory.style.color = c.numColor;
    bmiCategory.style.borderColor = c.border;
    if (bmiAdvice) bmiAdvice.textContent = c.adv;

    // Gauge: needle angle (-90deg to 90deg over BMI 15-40)
    if (bmiNeedle) {
      const angle = Math.max(-90, Math.min(90, ((bmi - 15) / 25) * 180 - 90));
      bmiNeedle.setAttribute('transform', `rotate(${angle} 100 110)`);
    }
    // Gauge: filled arc proportional to BMI
    if (bmiGaugeArc) {
      const pct = Math.max(0, Math.min(1, (bmi - 15) / 25));
      const filled = pct * ARC_LEN;
      bmiGaugeArc.setAttribute('stroke-dasharray', `${filled} ${ARC_LEN - filled}`);
    }

    updateSliderFill(heightInput);
    updateSliderFill(weightInput);
  }

  heightInput.addEventListener('input', calculateBMI);
  weightInput.addEventListener('input', calculateBMI);
  
  const ethnicityRadios = document.querySelectorAll('input[name="ethnicity"]');
  ethnicityRadios.forEach(r => r.addEventListener('change', calculateBMI));
  
  calculateBMI();
}

/* === Animated Counters === */
function initCounters() {
  const counters = document.querySelectorAll('.int-num[data-target], .about-stats-num[data-target]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(c => observer.observe(c));
}

/* === Journey Timeline Spine Fill === */
function initJourneySpine() {
  const fill = document.querySelector('.journey-spine-fill');
  if (!fill) return;

  const update = () => {
    const spine = document.querySelector('.journey-spine');
    if (!spine) return;
    const rect = spine.getBoundingClientRect();
    const vh = window.innerHeight;
    const center = vh * 0.55;
    // How much of the spine is above the trigger line
    const scrolled = Math.max(0, Math.min(rect.height, center - rect.top));
    fill.style.height = scrolled + 'px';
  };
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
}

function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const dur = 2000;
  const start = performance.now();

  function update(now) {
    const progress = Math.min((now - start) / dur, 1);
    const ease = 1 - (1 - progress) ** 3;
    const val = Math.floor(target * ease);
    el.textContent = val >= 1000 ? (val / 1000).toFixed(1) + 'K' : val;
    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = target >= 1000 ? target / 1000 + 'K' : target;
  }

  requestAnimationFrame(update);
}

/* === Form Handler === */
function initFormHandler() {
  const form = document.getElementById('appointmentForm');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const orig = btn.innerHTML;
    btn.innerHTML = `<svg class="spin" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10" stroke-opacity="0.25"/><path d="M12 2a10 10 0 0 1 10 10"/></svg> Sending...`;
    btn.disabled = true;

    await new Promise(r => setTimeout(r, 1500));

    btn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Request Sent!`;
    btn.style.background = '#25D366';

    setTimeout(() => {
      form.reset();
      btn.innerHTML = orig;
      btn.disabled = false;
      btn.style.background = '';
    }, 3000);
  });
}

/* === Back to Top === */
function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.pageYOffset > 500);
  }, { passive: true });

  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* === Hero Video === */
function initHeroVideo() {
  const video = document.querySelector('.hero-video');
  if (!video) return;

  // Force the looping + autoplay attributes programmatically too, in case
  // any markup stripping removed them.
  video.muted = true;
  video.loop = true;
  video.playsInline = true;
  video.autoplay = true;

  // Safety net: if the `loop` attribute ever fails (e.g. video streams that
  // don't have a clean end-of-stream), rewind and play again.
  video.addEventListener('ended', () => {
    video.currentTime = 0;
    video.play().catch(() => { /* ignore */ });
  });

  // Some browsers (esp. mobile) ignore `autoplay` even when muted is set.
  // Calling .play() explicitly — wrapped in a promise catch so it never throws.
  const tryPlay = () => {
    const p = video.play();
    if (p && typeof p.catch === 'function') p.catch(() => { /* autoplay blocked; poster shown */ });
  };
  tryPlay();

  // If the video ever gets paused (tab background, browser policy, etc.),
  // re-trigger playback on the next user-visible tick.
  video.addEventListener('pause', () => {
    if (video.currentTime >= video.duration - 0.1) return; // ended-handler will run
    setTimeout(tryPlay, 250);
  });

  // Pause when off-screen to save battery/CPU; resume on return.
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) tryPlay();
        else video.pause();
      });
    }, { threshold: 0.25 });
    io.observe(video);
  }
}

/* === Success Stories Carousel === */
function initSuccessCarousel() {
  const track = document.querySelector('.success-track');
  const carousel = document.querySelector('.success-carousel');
  const slides = document.querySelectorAll('.success-slide');
  const dots = document.querySelectorAll('.success-dot');
  const thumbs = document.querySelectorAll('.ss-thumb');
  const prevBtn = document.querySelector('.success-prev');
  const nextBtn = document.querySelector('.success-next');

  if (!track || !carousel || slides.length === 0) return;

  // Tell CSS how many slides we have so the track can size itself
  track.style.setProperty('--slide-count', String(slides.length));

  let current = 0;
  let interval;

  function goTo(i) {
    current = (i + slides.length) % slides.length;
    // Move by the carousel's actual width in pixels (one slide = one viewport)
    const slideWidth = carousel.getBoundingClientRect().width;
    track.style.transform = `translateX(-${current * slideWidth}px)`;
    dots.forEach((d, j) => d.classList.toggle('active', j === current));
    thumbs.forEach((t, j) => t.classList.toggle('active', j === current));
  }

  // Recalculate on resize so it stays correct on window resize / orientation change
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => goTo(current), 100);
  });

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  prevBtn?.addEventListener('click', () => { prev(); resetInterval(); });
  nextBtn?.addEventListener('click', () => { next(); resetInterval(); });
  dots.forEach((d, i) => d.addEventListener('click', () => { goTo(i); resetInterval(); }));
  thumbs.forEach((t, i) => t.addEventListener('click', () => { goTo(i); resetInterval(); }));

  function resetInterval() {
    clearInterval(interval);
    interval = setInterval(next, 6000);
  }

  let tx = 0;
  track.addEventListener('touchstart', e => { tx = e.changedTouches[0].screenX; clearInterval(interval); }, { passive: true });
  track.addEventListener('touchend', e => {
    const diff = tx - e.changedTouches[0].screenX;
    if (diff > 50) next(); else if (diff < -50) prev();
    resetInterval();
  }, { passive: true });

  resetInterval();
}

/* === Video List Click === */
function initVideoList() {
  const items = document.querySelectorAll('.videos-list-item');
  const mainIframe = document.getElementById('mainVideo');
  const mainInfo = document.querySelector('.videos-main-info');
  if (!items.length || !mainIframe) return;
  items.forEach(item => {
    item.addEventListener('click', () => {
      const videoId = item.dataset.video;
      const title = item.dataset.title;
      const cat = item.dataset.cat;
      mainIframe.src = `https://www.youtube.com/embed/${videoId}`;
      const h3 = mainInfo?.querySelector('h3');
      const span = mainInfo?.querySelector('span');
      if (h3) h3.textContent = title;
      if (span) span.textContent = cat;
      items.forEach(i => i.classList.remove('active'));
      item.classList.add('active');
    });
  });
}

/* === Peter's Fitness Factory === */
function initFitnessFactory() {
  const items = document.querySelectorAll('.fitness-card');
  if (!items.length) return;
  items.forEach(item => {
    item.addEventListener('click', () => {
      const videoId = item.dataset.video;
      const title = item.dataset.title;
      const mainIframe = document.getElementById('mainVideo');
      const mainInfo = document.querySelector('.videos-main-info');
      if (mainIframe) mainIframe.src = `https://www.youtube.com/embed/${videoId}`;
      if (mainInfo) {
        const h3 = mainInfo.querySelector('h3');
        const span = mainInfo.querySelector('span');
        if (h3) h3.textContent = title;
        if (span) span.textContent = "Peter's Fitness Factory";
      }
    });
  });
}

/* === FAQ Category Filter === */
function initFAQFilter() {
  const cats = document.querySelectorAll('.faq-cat');
  const cards = document.querySelectorAll('.faq-card');

  cats.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.cat;

      // Toggle active state
      cats.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Filter cards with animation
      cards.forEach(card => {
        const cardCat = card.dataset.category;
        if (cat === 'all' || cardCat === cat) {
          card.style.display = 'block';
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          requestAnimationFrame(() => {
            card.style.transition = 'all 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          });
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// Initialize if present
document.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector('.faq-cat')) {
    initFAQFilter();
  }
});

/* === Spinner CSS === */
const style = document.createElement('style');
style.textContent = `
  @keyframes spin { to { transform: rotate(360deg); } }
  .spin { animation: spin 1s linear infinite; }
`;
document.head.appendChild(style);

/* === Conferences Tab Filter === */
function initConferenceTabs() {
  const tabs = document.querySelectorAll('.about-conf-tab');
  const timelines = {
    recent: document.querySelector('.about-conf-timeline--recent'),
    '2010s': document.querySelector('.about-conf-timeline--2010s'),
    older: document.querySelector('.about-conf-timeline--older')
  };

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const year = tab.dataset.year;
      Object.values(timelines).forEach(tl => {
        if (tl) tl.style.display = 'none';
      });
      if (timelines[year]) {
        timelines[year].style.display = 'block';
      }
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector('.about-conf-tab')) {
    initConferenceTabs();
  }
});