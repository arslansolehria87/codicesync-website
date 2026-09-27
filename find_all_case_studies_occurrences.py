import sys

with open(r'F:\codicesync\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    l = line.lower()
    if any(k in l for k in ['shaki', 'javed', 'chaajao', 'childlife', 'tip pakistan', 'our best', 'works']):
        safe_line = line.strip()[:150].encode('ascii', 'ignore').decode('ascii')
        print(f"Line {idx+1}: {safe_line}")
