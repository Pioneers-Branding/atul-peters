import re

file_path = "e:/atul-peters/atul-peters/laparoscopic-surgery-in-delhi.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Meta Description & Keywords
content = content.replace(
    'content="Seeking the best gallbladder surgery in Delhi? Consult Dr. Atul Peters at Max Smart Super Speciality Hospital, Saket - New Delhi. Gold standard 4K Laparoscopic &amp; Robotic Cholecystectomy with Critical View of Safety (CVS), virtually invisible scars, and 24-hour discharge."',
    'content="Seeking the best laparoscopic surgery in Delhi? Consult Dr. Atul Peters. Experience gold standard 4K Laparoscopic &amp; Robotic Surgery for various conditions with virtually invisible scars and 24-hour discharge."'
)
content = content.replace(
    'content="best gallbladder surgery in Delhi, laparoscopic cholecystectomy Delhi, gallstone removal surgery Delhi NCR, robotic gallbladder surgery India, gallbladder stone treatment cost Delhi, keyhole surgery, cholelithiasis specialist Delhi, Dr Atul Peters"',
    'content="best laparoscopic surgery in Delhi, keyhole surgery Delhi, minimal access surgery India, Dr Atul Peters laparoscopic surgeon, robotic surgery Delhi NCR, minimally invasive surgery"'
)
content = content.replace(
    '<meta content="Best Gallbladder Surgery in Delhi | Dr. Atul Peters - Max Smart Super Speciality Hospital, Saket"\n    property="og:title" />',
    '<meta content="Best Laparoscopic Surgery in Delhi | Dr. Atul Peters - Max Smart Super Speciality Hospital, Saket"\n    property="og:title" />'
)
content = content.replace(
    '<meta\n    content="https://www.atulpeters.com/best-gallbladder-surgery-in-delhi" property="og:url" />',
    '<meta\n    content="https://www.atulpeters.com/laparoscopic-surgery-in-delhi" property="og:url" />'
)

# 2. JSON-LD replacement (just simplify it to be generic)
json_ld_old = r'"alternateName": "Keyhole Gallbladder Removal Surgery / Gallstone Removal Surgery / Cholelithiasis Surgery",.*?gallstones cannot form in the gallbladder again'
# It's better to just regex out the gallbladder questions from JSON-LD
content = re.sub(r'\{[^}]*"name": "Why is it necessary to remove the entire gallbladder.*?\}[,]*', '', content, flags=re.DOTALL)
content = re.sub(r'\{[^}]*"name": "How will my body digest food normally after my gallbladder is removed.*?\}[,]*', '', content, flags=re.DOTALL)
content = re.sub(r'\{[^}]*"name": "Why do gallstones form and can they be dissolved.*?\}[,]*', '', content, flags=re.DOTALL)
content = re.sub(r'\{[^}]*"name": "How soon can I walk, eat, and return to work after gallbladder surgery in Delhi.*?\}[,]*', '', content, flags=re.DOTALL)
content = re.sub(r'\{[^}]*"name": "Is laparoscopic and robotic gallbladder surgery covered by health insurance in India.*?\}[,]*', '', content, flags=re.DOTALL)

# Fix alternateName etc
content = content.replace('"alternateName": "Keyhole Gallbladder Removal Surgery / Gallstone Removal Surgery / Cholelithiasis Surgery",', '"alternateName": "Keyhole Surgery / Minimal Access Surgery",')
content = content.replace('"description": "Gold standard minimally invasive surgery to remove a diseased gallbladder containing gallstones (cholelithiasis), polyps, or acute/chronic inflammation (cholecystitis). Performed through 3 to 4 tiny keyhole incisions using 4K Ultra HD visualization and Critical View of Safety (CVS) protocols to ensure 100% biliary duct safety.",', '"description": "Gold standard minimally invasive surgery performed through 3 to 4 tiny keyhole incisions using 4K Ultra HD visualization.",')
content = content.replace('"bodyLocation": "Upper Right Abdomen (Gallbladder, Biliary Tree, Liver Bed)",', '"bodyLocation": "Abdomen",')
content = content.replace('"url": "https://www.atulpeters.com/best-gallbladder-surgery-in-delhi",', '"url": "https://www.atulpeters.com/laparoscopic-surgery-in-delhi",')
content = content.replace('"name": "Best Gallbladder Surgery in Delhi"', '"name": "Best Laparoscopic Surgery in Delhi"')
content = content.replace('"item": "https://www.atulpeters.com/best-gallbladder-surgery-in-delhi"', '"item": "https://www.atulpeters.com/laparoscopic-surgery-in-delhi"')


# 3. Breadcrumb & Hero
content = content.replace('<span class="nc-breadcrumb-current">Best Gallbladder Surgery in Delhi</span>', '<span class="nc-breadcrumb-current">Best Laparoscopic Surgery in Delhi</span>')
content = content.replace('src="assets/img/gallbladder-hero-img.webp"', 'src="assets/img/surgery-img.jpg"')

# 4. Symptoms / Overview
content = content.replace('The gallbladder is a pear-shaped organ located beneath your liver on the right side of your abdomen. It stores', 'Laparoscopic surgery is used to treat a wide variety of abdominal conditions. It involves')
content = content.replace('Alt="Gallbladder Anatomy"', 'Alt="Laparoscopic Surgery Anatomy"')


# 5. FAQs
content = re.sub(r'<div class="gb-faq-item">.*?Will I experience weight gain or weight loss after my gallbladder is removed\?.*?</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="gb-faq-item">.*?Can gallstones form again after my gallbladder is surgically removed\?.*?</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="gb-faq-item">.*?Why choose Dr. Atul Peters at Max Smart Super Speciality Hospital, Saket for gallbladder.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# 6. Appointment Title
content = content.replace('Ready to Learn if <span class="appt-title-accent">Gallbladder Surgery</span><br />is Right for You?', 'Ready to Learn if <span class="appt-title-accent">Laparoscopic Surgery</span><br />is Right for You?')


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
