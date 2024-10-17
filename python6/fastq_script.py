#!usr/bin/env python3

# go through each line of .fastq file
# count number of lines
# count number of characters
# report average line length

with open('/Users/pfb2024/pfb2024/files/Python_06.fastq') as f:
	count = 0
	char_count = 0
	for line in f:
		count += 1
		for word in line:
			char_count += 1
print(f'total lines: {count}, total chars: {char_count}')
print(f'average line length: {char_count/count}')