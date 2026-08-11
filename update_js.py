import re

files = ['hernia-surgery-in-delhi.html', 'best-gallbladder-surgery-in-delhi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    old_js = '''      window.addEventListener('scroll', function () {
        let current = '';
        sections.forEach(function (section) {
          const sectionTop = section.offsetTop - 140;
          if (window.pageYOffset >= sectionTop) {
            current = section.getAttribute('id');
          }
        });

        navLinks.forEach(function (link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
          }
        });
      });'''

    new_js = '''      let lastActive = '';
      window.addEventListener('scroll', function () {
        let current = '';
        sections.forEach(function (section) {
          const sectionTop = section.offsetTop - 140;
          if (window.pageYOffset >= sectionTop) {
            current = section.getAttribute('id');
          }
        });

        if (current !== lastActive) {
          lastActive = current;
          navLinks.forEach(function (link) {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
              link.classList.add('active');
              if (slider) {
                link.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
              }
            }
          });
        }
      });'''
      
    html = html.replace(old_js, new_js)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("JS updated.")
