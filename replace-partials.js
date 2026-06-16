const fs = require('fs');
const path = require('path');

const files = [
  'index.html',
  'index2.html',
  'about.html',
  'weight-loss.html',
  'roux-en-y-gastric-bypass.html'
];

for (const file of files) {
  const filePath = path.join(__dirname, file);
  if (!fs.existsSync(filePath)) continue;

  let content = fs.readFileSync(filePath, 'utf8');

  // Replace Header
  // The header starts with <!-- Top Bar --> or similar, up to </nav>
  content = content.replace(/<!-- Top Bar -->[\s\S]*?<\/nav>/, '<div id="header-placeholder"></div>');

  // Replace Footer
  // The footer starts with <footer ...> up to </footer>
  content = content.replace(/<footer[\s\S]*?<\/footer>/, '<div id="footer-placeholder"></div>');

  // Remove the active nav injector script if it exists
  content = content.replace(/<script>\s*\(\s*function\s*\(\)\s*\{[\s\S]*?var\s+p\s*=\s*'[^']+';[\s\S]*?\}\s*\)\s*\(\)\s*;\s*<\/script>/, '');

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Processed ${file}`);
}
