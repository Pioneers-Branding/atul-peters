import re

with open(r'e:\atul-peters\atul-peters\robotic-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. how-it-works -> da-vinci-surgeon-console.png
html = re.sub(
    r'(<section\s+class=\"gb-section gb-section--alt\"\s+id=\"how-it-works\")>',
    r'\1 style="position: relative; overflow: hidden;">\n    <div class="gb-sketch-watermark" style="background-image: url(\'assets/img/da-vinci-surgeon-console.png\'); width: 450px; height: 450px; top: 10%; right: -5%; opacity: 0.12; transform: rotate(5deg);"></div>',
    html,
    count=1
)

# 2. benefits -> da-vinci-patient-cart.png
html = re.sub(
    r'(<section\s+class=\"gb-section\"\s+id=\"benefits\")>',
    r'\1 style="position: relative; overflow: hidden;">\n    <div class="gb-sketch-watermark" style="background-image: url(\'assets/img/da-vinci-patient-cart.png\'); width: 450px; height: 450px; bottom: 5%; left: -5%; opacity: 0.12; transform: rotate(-5deg);"></div>',
    html,
    count=1
)

# 3. procedures -> sketch_robotic_surgery_1786011760417.png
html = re.sub(
    r'(<section\s+class=\"gb-section\"\s+id=\"procedures\")>',
    r'\1 style="position: relative; overflow: hidden; background-color: #f0f7ff;">\n    <div class="gb-sketch-watermark" style="background-image: url(\'assets/img/sketch_robotic_surgery_1786011760417.png\'); width: 500px; height: 500px; top: 20%; left: -5%; opacity: 0.08; transform: rotate(3deg) scaleX(-1);"></div>',
    html,
    count=1
)

# 4. dr-peters -> sketch_atul_peters_transparent.png
html = re.sub(
    r'(<section\s+class=\"gb-section gb-section--alt\"\s+id=\"dr-peters\")>',
    r'\1 style="position: relative; overflow: hidden;">\n    <div class="gb-sketch-watermark" style="background-image: url(\'assets/img/sketch_atul_peters_transparent.png\'); width: 400px; height: 400px; bottom: 0; right: -5%; opacity: 0.1; transform: rotate(-5deg);"></div>',
    html,
    count=1
)

# Make sure containers are relative z-10 inside these sections
html = re.sub(r'(<section[^>]*id=\"(?:how-it-works|benefits|procedures|dr-peters)\"[^>]*>.*?)<div class=\"container\">', r'\1<div class="container relative z-10">', html, flags=re.DOTALL)

with open(r'e:\atul-peters\atul-peters\robotic-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated robotic-surgery-in-delhi.html successfully!')
