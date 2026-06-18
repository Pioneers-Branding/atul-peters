const fs = require('fs');
let html = fs.readFileSync('travel-desk.html', 'utf8');
html = html.replace(/<div class="faq-answer">\s*<p>/g, '<div class="faq-answer"><div class="faq-answer-inner"><p>');
html = html.replace(/<\/p>\s*<\/div>/g, '</p></div></div>');
fs.writeFileSync('travel-desk.html', html);
console.log('Fixed HTML wrapper');

// Now let's fix styles.css so .faq-answer has NO padding, but .faq-answer-inner has it
let css = fs.readFileSync('styles.css', 'utf8');
if (!css.includes('.faq-answer { padding: 0 !important; border: none !important; }')) {
  css += `\n/* Fix FAQ Accordion Padding */\n.faq-accordion .faq-answer { padding: 0 !important; border: none !important; }\n`;
  fs.writeFileSync('styles.css', css);
  console.log('Fixed CSS padding');
}
