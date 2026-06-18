const fs = require('fs');
const path = require('path');

const headerHTML = fs.readFileSync(path.join(__dirname, 'partials/header.html'), 'utf8');
const footerHTML = fs.readFileSync(path.join(__dirname, 'partials/footer.html'), 'utf8');

const headerJS = `document.write(\`${headerHTML.replace(/`/g, '\\`').replace(/\$/g, '\\$')}\`);`;
const footerJS = `document.write(\`${footerHTML.replace(/`/g, '\\`').replace(/\$/g, '\\$')}\`);`;

fs.writeFileSync(path.join(__dirname, 'partials/header.js'), headerJS, 'utf8');
fs.writeFileSync(path.join(__dirname, 'partials/footer.js'), footerJS, 'utf8');

console.log('Generated header.js and footer.js');
