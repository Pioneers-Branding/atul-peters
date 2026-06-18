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

  content = content.replace(/<div id="header-placeholder"><\/div>/, '<script src="partials/header.js"></script>');
  content = content.replace(/<div id="footer-placeholder"><\/div>/, '<script src="partials/footer.js"></script>');

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Processed ${file}`);
}
