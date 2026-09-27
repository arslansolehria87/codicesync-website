import re

with open(r'F:\codicesync\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Marquee 1 items
marquee_1_items = ['Data Driven Funnels', 'CRM & Automation Setup', 'Scalable Infrastructure', 'Conversion Focused Design', 'High Security & Compliance', 'Advanced Analytics', 'Fast Performance', 'Seamless Integrations']

# Replace Marquee 2 text ("Let’s Get Started") with CodiceSync brand slogan
content = content.replace('Let’s Get Started', 'CodiceSync — Smarter Digital Solutions. Built for Growth.')
content = content.replace("Let's Get Started", 'CodiceSync — Smarter Digital Solutions. Built for Growth.')

with open(r'F:\codicesync\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer marquee text updated with CodiceSync brand messaging!")
