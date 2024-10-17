#!usr/bin/env python3

# print the reverse complement of each sequence. print in FASTA format (sequence name 
# and note in the description that this is reverse complement)

seqs = {}

# open the file, create dictionary where key is gene name??? and value is sequence
with open('/Users/pfb2024/pfb2024/files/Python_06.seq.txt') as f:
    for line in f:
        line = line.rstrip()
        gene, sequence = line.split('\t')
        seqs[gene] = sequence

# iterate through the dictionary for each sequence entry of fasta file, then iterate through each base
# in the sequence to give the complement, then reverse it and print out reverse complement.
for key in seqs.keys():
	comp = ''
	rev_comp = ''
	for base in seqs[key]:
		if base == 'A':
			comp = comp + ('T')
		elif base == 'T':
			comp = comp + ('A')
		elif base == 'C':
			comp = comp + ('G')
		elif base == 'G':
			comp = comp + ('C')
		else:
			print('error! did not recognize base')
	for base in comp[::-1]:
		rev_comp = rev_comp + base
	print(f'>{key} Reverse Complement {rev_comp}')