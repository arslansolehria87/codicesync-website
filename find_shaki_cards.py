with open(r'F:\codicesync\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines):
    if 'id="shaki' in l or 'id=\'shaki' in l or 'Our Best' in l:
        print(idx+1, l.strip())
