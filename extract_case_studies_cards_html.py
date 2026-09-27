with open(r'F:\codicesync\codicesync\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('elementor-element-bad6166')
print("bad6166 pos:", pos)

if pos != -1:
    print(content[pos-100:pos+8000])
