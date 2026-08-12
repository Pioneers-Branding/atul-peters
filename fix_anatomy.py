import re

with open(r'e:\atul-peters\atul-peters\laparoscopic-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert missing CSS for gb-hotspot-card
css_to_insert = """
          .gb-info-hotspots {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 1.5rem;
          }

          .gb-hotspot-card {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.9);
            border-radius: 1.5rem;
            padding: 1.75rem;
            display: flex;
            gap: 1.5rem;
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
            cursor: pointer;
          }

          .gb-hotspot-card:hover,
          .gb-hotspot-card.active {
            background: #ffffff;
            transform: translateX(12px) translateY(-2px);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.08);
            border-left: 6px solid #3182ce;
          }

          @media (max-width: 991px) {
            .gb-hotspot-card:hover,
            .gb-hotspot-card.active {
              transform: translateY(-5px);
            }
          }

          .gb-hotspot-card:nth-child(1).active,
          .gb-hotspot-card:nth-child(2).active,
          .gb-hotspot-card:nth-child(3).active {
            border-left-color: #2A7AB5;
          }

          .gb-hotspot-num {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            background: #0A1E30;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: 800;
            font-size: 1.15rem;
            flex-shrink: 0;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
          }

          .gb-hotspot-card:nth-child(1) .gb-hotspot-num,
          .gb-hotspot-card:nth-child(2) .gb-hotspot-num,
          .gb-hotspot-card:nth-child(3) .gb-hotspot-num {
            background: linear-gradient(135deg, #2A7AB5, #154779);
            color: #fff;
          }

          .gb-hotspot-text h4 {
            margin: 0 0 0.5rem 0;
            font-family: 'DM Sans', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #1a202c;
          }

          .gb-hotspot-text p {
            margin: 0;
            font-size: 0.98rem;
            color: #4a5568;
            line-height: 1.6;
          }
"""

# Replace in Style 3
match = re.search(r'(\.gb-anatomy-svg \{.*?filter: drop-shadow\(0 10px 15px rgba\(0, 0, 0, 0\.4\)\);\n    \})', html, re.DOTALL)
if match:
    html = html[:match.end()] + "\n" + css_to_insert + html[match.end():]

# 2. Change the image from laparoscopic-anatomy-infographic.png to sketch_laparoscopic_abdomen_1786011745049.png
# Wait, let's look at the available images again. 
# sketch_laparoscopic_abdomen_1786011745049.png
html = html.replace('laparoscopic-anatomy-infographic.png', 'sketch_laparoscopic_abdomen_1786011745049.png')

# Wait! The original gb-anatomy-svg-box has a dark background. A sketch image usually has a white/transparent background and might need filter adjustments or a light background.
# Let's change the background of gb-anatomy-svg-box from dark blue gradient to a light gradient if we're using a sketch.
# Actually, I'll just change the background to a soft light blue so the sketch is visible.
html = re.sub(
    r'\.gb-anatomy-svg-box \{\s*background: linear-gradient\(135deg, #0A1E30 0%, #154779 100%\);',
    r'.gb-anatomy-svg-box {\n      background: linear-gradient(135deg, #f0f7ff 0%, #e2e8f0 100%);',
    html
)

with open(r'e:\atul-peters\atul-peters\laparoscopic-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixes applied successfully!")
