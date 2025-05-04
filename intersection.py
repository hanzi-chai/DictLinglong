from encodings.punycode import T
import os

dicts = {}
ls = set()
union = set()
for file in [f for f in os.listdir("纯词库") if os.path.isfile(f"纯词库/{f}")]:
	with open(f"纯词库/{file}", 'r', encoding='utf-8') as f:
		file_is_lansan = False
		if file == '蓝三.txt':
			file_is_lansan = True
		for line in f:
			word = line.strip()
			union.add(word)
			if word in dicts:
				dicts[word] += 1
			else:
				dicts[word] = 1
			if file_is_lansan:
				ls.add(word)

result = [x for x in ls if dicts[x] > 3]

with open('交集.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(result)))

with open('并集.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(sorted(union)))
