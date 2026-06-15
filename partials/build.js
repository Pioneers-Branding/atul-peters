/* ============================================
   BUILD SCRIPT — Injects partials into HTML files
   Run with:  node partials/build.js
   ============================================ */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PARTIALS = path.join(ROOT, 'partials');

const HEADER_PATH = path.join(PARTIALS, 'header.html');
const FOOTER_PATH = path.join(PARTIALS, 'footer.html');

const HEADER_PLACEHOLDER = /<!-- ===== SHARED HEADER \(loaded from partials\/header\.html\) ===== -->[\s\S]*?<!-- ===== END SHARED HEADER ===== -->/;
const FOOTER_PLACEHOLDER = /<!-- ===== SHARED FOOTER \(loaded from partials\/footer\.html\) ===== -->[\s\S]*?<!-- ===== END SHARED FOOTER ===== -->/;

const ACTIVE_NAV_PATTERN = /<!-- ACTIVE_NAV:([\w-]+) -->/g;

const HTML_FILES = [
  'index.html',
  'about.html',
  'weight-loss.html',
  'roux-en-y-gastric-bypass.html',
];

function build() {
  const header = fs.readFileSync(HEADER_PATH, 'utf8');
  const footer = fs.readFileSync(FOOTER_PATH, 'utf8');

  let updated = 0;

  for (const file of HTML_FILES) {
    const filePath = path.join(ROOT, file);
    if (!fs.existsSync(filePath)) {
      console.log(`  [SKIP] ${file} (not found)`);
      continue;
    }

    let html = fs.readFileSync(filePath, 'utf8');
    const original = html;

    // Determine which nav link should be active for this page
    const pageBase = file.replace('.html', '');

    // Inject active nav class on the right link
    const activeAdder = `
<script>
  (function(){
    var p = '${file}';
    document.querySelectorAll('.navbar .nav-link').forEach(function(l){
      var href = (l.getAttribute('href') || '').split('#')[0];
      if (href === p) l.classList.add('nav-link--active');
    });
  })();
</script>
`;

    // Replace header placeholder
    if (HEADER_PLACEHOLDER.test(html)) {
      html = html.replace(HEADER_PLACEHOLDER, header);
    }
    // Replace footer placeholder
    if (FOOTER_PLACEHOLDER.test(html)) {
      html = html.replace(FOOTER_PLACEHOLDER, footer);
    }
    // Remove the layout.js script tag
    html = html.replace(/\s*<script src="partials\/layout\.js"><\/script>/g, '');
    // Inject the active nav script right before </body>
    if (!html.includes('// -- ACTIVE NAV INJECTOR --')) {
      html = html.replace('</body>', '  // -- ACTIVE NAV INJECTOR --\n' + activeAdder + '</body>');
    }

    if (html !== original) {
      fs.writeFileSync(filePath, html, 'utf8');
      console.log(`  [OK]   ${file}  (${(html.length / 1024).toFixed(1)} KB)`);
      updated++;
    } else {
      console.log(`  [NOOP] ${file}`);
    }
  }

  console.log(`\nDone. Updated ${updated} file(s).`);
  console.log('Header source:  partials/header.html');
  console.log('Footer source:  partials/footer.html');
  console.log('\nTo re-build:    node partials/build.js');
}

build();
