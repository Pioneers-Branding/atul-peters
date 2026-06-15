/* ============================================
   SHARED LAYOUT INJECTOR
   Loads header & footer partials, then marks
   the active nav link based on the current page.
   ============================================ */

(function () {
  'use strict';

  // Determine base path for partials (works for root and subfolders)
  function getPartialBase() {
    // partials/ folder is sibling of the HTML files (root level)
    return 'partials/';
  }

  // Cache buster — update this to force re-fetch on deploy
  const CACHE_BUST = 'v1';

  /**
   * Fetch a partial HTML file and inject it into a target element.
   */
  async function loadPartial(targetSelector, partialPath) {
    const target = document.querySelector(targetSelector);
    if (!target) return;

    try {
      const res = await fetch(partialPath + '?_=' + CACHE_BUST);
      if (!res.ok) throw new Error('Failed to load ' + partialPath);
      const html = await res.text();
      target.innerHTML = html;
    } catch (err) {
      console.error('[layout] ' + err.message);
    }
  }

  /**
   * Mark the nav link that matches the current page as active.
   * Match by data-page attribute or by href ending.
   */
  function setActiveNavLink() {
    const path = window.location.pathname.split('/').pop() || 'index.html';

    document.querySelectorAll('.navbar .nav-link').forEach((link) => {
      const href = (link.getAttribute('href') || '').split('#')[0];
      const dataPage = link.getAttribute('data-page');
      const linkFile = href.split('/').pop();

      // Skip placeholder "#" links
      if (!href || href === '#') return;

      // Direct file match
      if (linkFile === path) {
        link.classList.add('nav-link--active');
        return;
      }

      // data-page match (e.g. weight-loss.html highlights the Weight Loss nav)
      if (dataPage && (dataPage + '.html') === path) {
        link.classList.add('nav-link--active');
      }
    });
  }

  /**
   * Wire up the mobile nav toggle after the header is injected.
   */
  function initNavToggle() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navLinks');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
      toggle.classList.toggle('open');
      document.body.classList.toggle('nav-open');
    });

    // Close on link click (mobile)
    menu.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        menu.classList.remove('open');
        toggle.classList.remove('open');
        document.body.classList.remove('nav-open');
      });
    });
  }

  /**
   * Sticky-nav background swap on scroll.
   */
  function initStickyNav() {
    const nav = document.getElementById('navbar');
    if (!nav) return;

    const onScroll = () => {
      if (window.scrollY > 30) {
        nav.classList.add('navbar--scrolled');
      } else {
        nav.classList.remove('navbar--scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /**
   * Re-run any custom init that depended on the header/footer being in the DOM.
   * Pages can listen for this event to do their own post-inject work.
   */
  function dispatchReady() {
    document.dispatchEvent(new CustomEvent('partials:ready'));
  }

  /**
   * Entry point: load header + footer, then run post-inject init.
   */
  async function init() {
    const base = getPartialBase();

    await Promise.all([
      loadPartial('[data-include="header"]', base + 'header.html'),
      loadPartial('[data-include="footer"]', base + 'footer.html'),
    ]);

    setActiveNavLink();
    initNavToggle();
    initStickyNav();
    dispatchReady();
  }

  // Start as soon as DOM is parsed
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
