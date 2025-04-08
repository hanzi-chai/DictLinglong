from encodings.punycode import T
import os

dicts = {}
ls = set()
for file in [f for f in os.listdir("纯词库") if os.path.isfile(f"纯词库/{f}")]:
	with open(f"纯词库/{file}", 'r', encoding='utf-8') as f:
		file_is_lansan = False
		if file == '蓝三.txt':
			file_is_lansan = True
		for line in f:
			word = line.strip()
			if word in dicts:
				dicts[word] += 1
			else:
				dicts[word] = 1
			if file_is_lansan:
				ls.add(word)

result = [x[0] for x in dicts.items() if x[1] > 3 and x[0] in ls]

with open('交集.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(result))
