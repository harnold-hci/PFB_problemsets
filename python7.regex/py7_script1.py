#!usr/bin/env python3
import re

with open('/Users/pfb2024/pfb2024/files/Python_07_nobody.txt') as f:
	text = f.read()
	location = []
	for match in re.finditer(r'nobody', text, re.IGNORECASE):
			location.append(match.start())
	print(location)

name = 'henry'
with open('/Users/pfb2024/pfb2024/files/Python_07_nobody.txt') as f, open('./'+ name +'.txt', 'w') as write_file:
	text = f.read()
	write_file.write(re.sub(r'Nobody', name, text))