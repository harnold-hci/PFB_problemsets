#!usr/bin/env python3
import re

# find all the header lines in fasta
# starts w/ >, followed by seqID (no spaces), followed by descriptin (which could have >)

with open('/Users/pfb2024/pfb2024/files/Python_07.fasta') as f:
    temp_seq = ''
    for line in f:
        line = line.rstrip()
        header = re.search(r'>(\w+)(.*)', line)
        if header:
            print(f'id:{header.group(1)} desc:{header.group(2)}')
            temp_seq = ''
        else:
            temp_seq = temp_seq + line
    print(temp_seq)
    #im not doing this shit rn
        
        # seq = re.search(r'\w+\s')
        # print(f'id:{header.group(1)} desc:{header.group(2)}')
