const https = require('https');
const fs = require('fs');

https.get('https://www.atulpeters.com/bmi-calculator', (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    let text = data.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
                   .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
                   .replace(/<[^>]+>/g, '\n');
    let lines = text.split('\n').map(l=>l.trim()).filter(l=>l.length>0);
    
    // Find where the content starts
    let startIdx = lines.indexOf('BMI Calculator');
    let content = lines.slice(startIdx, startIdx + 30).join('\n');
    fs.writeFileSync('bmi-raw.txt', content);
    console.log('Done');
  });
});
