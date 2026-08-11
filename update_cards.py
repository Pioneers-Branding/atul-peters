import re

with open('hernia-surgery-in-delhi.html', 'r', encoding='utf-8') as f:
    hr_html = f.read()

# Enhance .hr-card hover effect to match gb-card
hr_html = re.sub(r'(\.hr-card:hover \{.*?transform: translateY\()(-5px)(\).*?box-shadow: 0 )(15px 30px)( rgba\(0, 0, 0, 0.1\);.*?\})', r'\g<1>-10px\g<3>25px 50px\g<5>', hr_html, flags=re.DOTALL)

# Add glassmorphism to .hr-quick-nav
hr_html = re.sub(r'(\.hr-quick-nav \{.*?background: )(rgba\(255, 255, 255, 0.95\))(.*?\})', r'\g<1>rgba(255, 255, 255, 0.8)\n    backdrop-filter: blur(12px);\n    -webkit-backdrop-filter: blur(12px);\n    border-bottom: 1px solid rgba(255, 255, 255, 0.3);\g<3>', hr_html, flags=re.DOTALL)

# Apply better hover effect to .hr-type-card
hr_html = re.sub(r'(\.hr-type-card:hover \{.*?transform: translateY\()(-5px)(\).*?box-shadow: 0 )(15px 30px)( rgba\(0,0,0,0.1\);.*?\})', r'\g<1>-8px\g<3>20px 40px\g<5>', hr_html, flags=re.DOTALL)

with open('hernia-surgery-in-delhi.html', 'w', encoding='utf-8') as f:
    f.write(hr_html)

print("Card effects updated.")
