#!usr/bin/env python3
from Bio import SeqIO
import re
ifh = '/Users/pfb2024/uniprot_sprot.fasta'

ids = []
desc = []

for seq_record in SeqIO.parse(ifh, 'fasta'):
    ids.append(seq_record.id)
    desc.append(seq_record.description)
print(len(ids))
# fasta file contains protein sequence,  572214 records, seems intact?

count = {}
for sample in desc:
    # count.append(re.search(r'OS=[\w\s]+', sample))
    found = re.search(r'(OS=[\w\s]+)', sample)
    if found not in count.keys():
        count[found.group(1)] = 1
    else:
        count[found.group(1)] += 1
print(count)

# found = re.search(r'OS=Salmonella paratyphi B')
print(found)

'''
Here the genus is Salmonella and the species is paratyphi.
 There is also a strain 'B (strain ATCC BAA-1250 / SPB7). You can ignore this part. 
 Using regular expressions, extract just the genus and species and count the number 
 of sequences present for that genus/species combination. 
 List comprehensions make this kind of data processing quick to code, but
you might want to start by going step by step in a for loop.
'''