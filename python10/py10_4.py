#!usr/bin/env python3
import re
import argparse

# create a function to format string of DNA, each line no more than 60 nt

# take in fasta file name from command line
# take in max length of each line from command line

parser = argparse.ArgumentParser(description='a function that formats dna from FASTa file')
parser.add_argument('file', help = 'path to input fasta filename')
parser.add_argument('nts', type=int, help='how many nucleotides per line')
args = parser.parse_args()
filename = args.file
width = args.nts
# if args.out:
#     print('writing output to', args.out)

# dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# width = 80

#'/Users/pfb2024/pfb2024/files/Python_08.fasta'
# read_file = '/Users/pfb2024/pfb2024/files/Python_08.fasta'
read_file = filename
write_file = './fasta_test.fasta'
gene_list = []
seqs = {}

def format_DNA(dna, wid):
    dna2 = ''
    for nt in re.findall(r'\w', dna):
        dna2 = dna2 + nt
    for i in range(0, len(dna2), wid+1):
        dna2 = dna2[:i] + '\n' + dna2[i:]
    i += (wid+1)
    if i % wid+1:
        final_cut = i - (i%(wid+1))
        dna2 = dna2[:final_cut] + '\n' + dna2[final_cut:]
    return dna2

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
        # have the generated dict of key and sequences, now just need to feed each sequence
        # into the method
    for gene in seqs.keys():
        # print(gene, format_DNA(seqs[gene], width))
        w.write(f'>{gene}{format_DNA(seqs[gene], width)}\n')



# print(format_DNA(filename, width))