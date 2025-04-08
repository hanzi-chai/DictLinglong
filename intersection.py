import os

dicts = []
for file in [f for f in os.listdir("纯词库") if os.path.isfile(f"纯词库/{f}")]:
	dict = set()
	with open(f"纯词库/{file}", 'r', encoding='utf-8') as f:
		for line in f:
			dict.add(line.strip())
	dicts.append(dict)

result = dicts[0]
for dict in dicts[1:]:
	result = result & dict

with open('交集.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(result))
