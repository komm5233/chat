#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

 
def convert(lines):
	preson = None
	Matt_word_count = 0
	Matt_sticker_count = 0
	Matt_image_count = 0
	Emma_word_count = 0
	Emma_sticker_count = 0
	Emma_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '統樂豬婆':
			if s[2] == '貼圖':
				Matt_sticker_count += 1
			elif s[2] == '圖片':
				Matt_image_count += 1
			else:
				for m in s[2:]:
					Matt_word_count += len(m)
		elif name == 'Chien':
			if s[2] == '貼圖':
				Emma_sticker_count += 1
			elif s[2] == '圖片':
				Emma_image_count += 1
			else:
				for m in s[2:]:
					Emma_word_count += len(m)
	print('Matt說了', Matt_word_count, '個字')
	print('傳了', Matt_sticker_count, '個貼圖，傳了', Matt_image_count, '個圖片')
	
	print('Emma說了', Emma_word_count, '個字')
	print('傳了', Emma_sticker_count, '個貼圖，傳了', Matt_image_count, '個圖片')

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('line_Emma.txt')
	lines = convert(lines)
	#write_file('ouput_line_Emma.txt', lines)

main()

