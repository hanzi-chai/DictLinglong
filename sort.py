dict = set()
with open('Dictlinglong.txt', 'r', encoding='utf-8') as f:
	for line in f:
		dict.add(line.strip())

with open('Dictlinglong.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(dict)))
