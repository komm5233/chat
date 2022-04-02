
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 換行 以及 preson = None
def convert(lines):
	new = []
	preson = None
	for line in lines:
		if line == '谷薏德':
			person = '谷薏德'
			continue
		if line == '簡聯振':
			person = '簡聯振'
			continue
		if person:
			new.append(person + ':' + line)
	return(new)

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')
	print(lines)

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('ouput.txt', lines)

main()

