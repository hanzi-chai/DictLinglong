dict = set()
with open('DictLinglong.txt', 'r', encoding='utf-8') as f:
	for line in f:
		dict.add(line.strip())

with open('DictLinglong.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(dict)))
