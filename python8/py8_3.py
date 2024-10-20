#!usr/bin/env python3
import re

# take a multi-FASTA file from user input
# calculate nucleotide composition for each sequence
# use datastructure to keep count
# print each sequence name and its composition in this format:
#  seqName\tA_count\tT_count\tG_count\tC_count

seqs = {}
gene_list = []
temp_seq = ''
count = 0
shift = 3

read_file = '/Users/pfb2024/pfb2024/files/Python_08.fasta'
write_file = './codon_frameshift_output.nt'

with open(read_file) as f, open(write_file, 'w') as w:
    for line in f:
        line = line.rstrip()
        header = None
        header = re.search(r'>(\w+)(.*)', line)
        base_list = []
        # if header, generate a new dict entry with that header name
        if header:
            gene_name = header.group(1)
            gene_list.append(gene_name)
            seqs[gene_name] = {}
            temp_seq = ''
        # if sequence: assign sequence to it's gene header
        else:
            # concat lines until i hit another header
            temp_seq = temp_seq + line
            seqs[gene_name] = temp_seq
    # now need to spit out 3 bases at a time
    # for each gene in the sequence dictionary
    for gene in seqs.keys():
        # return a list of codons from the sequence
        # iterates for each frameshift
        for i in range(1,shift+1):
            codon_list = re.findall(r'.{3}', seqs[gene][i:])
            w.write(f'{gene}-frame{i}-codons\n')
            cod = ''
            # print the codons in a line
            for codon in codon_list:
                cod = cod + codon + ' '
            cod = cod + '\n'
            w.write(cod)