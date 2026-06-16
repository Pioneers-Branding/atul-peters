const https = require('https');
const fs = require('fs');

https.get('https://www.atulpeters.com/disclaimer', (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    let parts = data.split('<div class="container">');
    // Usually the main content is in the second or third container
    let contentHtml = parts.length > 2 ? parts[2] : parts[1];
    
    // Stop at the footer
    if (contentHtml) {
        contentHtml = contentHtml.split('<footer>')[0];
    } else {
        contentHtml = data;
    }

    let text = contentHtml.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
                   .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
                   .replace(/<[^>]+>/g, '\n');
    let lines = text.split('\n').map(l=>l.trim()).filter(l=>l.length>0);
    
    fs.writeFileSync('disclaimer.txt', lines.join('\n'));
    console.log('Done writing disclaimer.txt');
  });
});
