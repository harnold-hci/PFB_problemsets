#!usr/bin/env python3

with open('/Users/pfb2024/pfb2024/files/Python_06.txt') as f, open('./lyrics_out.txt', 'w') as lyric_write:
	for line in f:
		line = line.rstrip()
		line = line.upper()
		print(line)
		lyric_write.write(line+'\n')

print('complete')