lines = []
with open('line_Emma2.txt', 'r', encoding='utf-8') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)

