const fs = require('fs');
let html = fs.readFileSync('nutrition-clinic.html', 'utf8');
html = html.replace(/<div class="faq-answer">\s*<p>/g, '<div class="faq-answer"><div class="faq-answer-inner"><p>');
html = html.replace(/<\/p>\s*<\/div>/g, '</p></div></div>');
fs.writeFileSync('nutrition-clinic.html', html);
console.log('Fixed HTML wrapper for nutrition-clinic.html');
