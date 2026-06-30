import re

with open('c:\\Users\\GC VENTURE\\Desktop\\v-s\\atul-peter\\weight-loss-surgery\\intra-gastric-balloon.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split the file by <section, but preserve the delimiter
parts = html.split('<section ')
head = parts[0]
blocks = ['<section ' + p for p in parts[1:]]

def find_block(identifier):
    for i, b in enumerate(blocks):
        if identifier in b:
            return i
    return -1

# Extract blocks in current order to ensure we grab everything correctly
# The identifiers here must be unique substrings
hero = blocks.pop(find_block('rygb-hero'))
overview = blocks.pop(find_block('id="overview"'))
how_it_works = blocks.pop(find_block('id="how-it-works"'))
candidate = blocks.pop(find_block('id="candidate"'))
types = blocks.pop(find_block('id="types"'))
benefits = blocks.pop(find_block('rygb-benefits'))
diet = blocks.pop(find_block('id="diet"'))
about = blocks.pop(find_block('id="about"'))
faq = blocks.pop(find_block('rygb-section--prose rygb-bg-alt'))
compare = blocks.pop(find_block('id="rygb-compare"'))
cost = blocks.pop(find_block('id="rygb-cost"'))
results = blocks.pop(find_block('id="rygb-results"'))
related = blocks.pop(find_block('id="rygb-related"'))
appointment = blocks.pop(find_block('id="appointment"'))

# SEO Optimized Order:
# 1. Hero
# 2. Overview (What is it?)
# 3. Types of Balloons
# 4. Compare Procedures
# 5. Am I a Candidate
# 6. Benefits
# 7. Real Patient Results
# 8. How it works
# 9. Diet & Lifestyle
# 10. Cost
# 11. About Dr Peters
# 12. FAQ
# 13. Related
# 14. Appointment

new_blocks = [
    hero,
    overview,
    types,
    compare,
    candidate,
    benefits,
    results,
    how_it_works,
    diet,
    cost,
    about,
    faq,
    related,
    appointment
]

# Write back
with open('c:\\Users\\GC VENTURE\\Desktop\\v-s\\atul-peter\\weight-loss-surgery\\intra-gastric-balloon.html', 'w', encoding='utf-8') as f:
    f.write(head + "".join(new_blocks) + "".join(blocks))

print("Successfully reordered sections!")
