import os
file_path = r'e:\atul-peters\atul-peters\weight-loss-surgery\mini-gastric-bypass.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Optimize sentence
text = text.replace('optimize fat loss and diabetes reversal.', 'optimize weight loss, diabetes reversal and other comorbidity resolution.')

# 2. Procedure name color
text = text.replace('Mini <span class="text-accent">Gastric Bypass</span>', 'Mini Gastric Bypass')

# 3. Free
text = text.replace('Book Free Consultation', 'Book Consultation')
text = text.replace('Free consultation.', 'Consultation.')
text = text.replace('Free evaluation', 'Expert evaluation')
text = text.replace('Free Consultation', 'Consultation')
text = text.replace('Request Free Consultation', 'Request Consultation')
text = text.replace('Free - No Obligation', 'No Obligation')
text = text.replace('Free – No Obligation', 'No Obligation')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Edited remaining MGB comments')
