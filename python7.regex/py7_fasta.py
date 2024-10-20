#!usr/bin/env python3
import re

# find all the header lines in fasta
# starts w/ >, followed by seqID (no spaces), followed by descriptin (which could have >)

with open('/Users/pfb2024/pfb2024/files/Python_07.fasta') as f:
    file = f.read()
    found = re.search(r'>(\w+)(.*)', file)
    print(f'id:{found.group(1)} desc:{found.group(2)}')
	
	# print(re.findall(r'>(\w+)(.*)', file))
    # print(.group(1))