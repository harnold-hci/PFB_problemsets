#!usr/bin/env python3
import re

# Apol R^AATTY -> R = A or G
# Y = C or T

# Write a regular expression to find and print all occurrences of the site in the following sequence

with open('/Users/pfb2024/pfb2024/files/Python_07_ApoI.fasta') as f:
    file = f.read()
    for cut in re.finditer(r'([A|G]AATT[C|T])', file):
        print(f'Cut: {cut.group(1)}, loc: {cut.start(1)}')
    cut_full = (re.sub(r'([A|G])(AATT[C|T])', r'\1^\2', file))
    print(cut_full)

cut_seq = re.sub(r'>\w+\s', '', cut_full)
cut_seq = re.sub(r'\s', '', cut_seq)
frags = cut_seq.split('^')
print(frags)

frag_dict = {}
frag_lens = []
for frag in frags:
    frag_dict[len(frag)] = frag
    frag_lens.append(len(frag))
print(frag_lens)
for length in sorted(frag_lens, reverse=True):
    print(frag_dict[length])