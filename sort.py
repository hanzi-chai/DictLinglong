dict = set()
with open('DictLinglong.txt', 'r', encoding='utf-8') as f:
	for line in f:
		dict.add(line.strip())

with open('DictLinglong.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(dict)))
	
origindict = set()
with open('交集.txt', 'r', encoding='utf-8') as f:
	for line in f:
		origindict.add(line.strip())

with open('增.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(dict.difference(origindict))))

with open('减.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(origindict.difference(dict))))
