#!usr/var/bin python3
import sys

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

count = 0
for mc in dna_list:
	print(f'{count}\t{len(mc)}\t{mc}')
	count += 1
