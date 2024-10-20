#!usr/bin/env python3
import re

# take a multi-FASTA file from user input
# calculate nucleotide composition for each sequence
# use datastructure to keep count
# print each sequence name and its composition in this format:
#  seqName\tA_count\tT_count\tG_count\tC_count

seqs = {}
gene_list = []
with open('/Users/pfb2024/pfb2024/files/Python_08.fasta') as f:
    for line in f:
        line = line.rstrip()
        header = None
        header = re.search(r'>(\w+)(.*)', line)
        base_list = []
        # if header, generate a new dict entry with that header name
        if header:
            gene_name = header.group(1)
            gene_list.append(gene_name)
            seqs[gene_name] = {'A':0, 'T':0, 'C':0, 'G':0}
        # if sequence: begin counting nucleotides
        else:
            # count each nucleotide
            a_bases = re.findall(r'A', line)
            t_bases = re.findall(r'T', line)
            c_bases = re.findall(r'C', line)
            g_bases = re.findall(r'G', line)
            # create list of all the instances of each base
            base_list = [a_bases, t_bases, c_bases, g_bases]
            # adds the bases to each dict entry
            for bases in base_list:
                if bases:
                    seqs[gene_name][bases[0]] += len(bases)
    for gene_name in gene_list:
        print(f'{gene_name}\t A:{seqs[gene_name]["A"]}\t T:{seqs[gene_name]['T']}\t C:{seqs[gene_name]['C']}\t G:{seqs[gene_name]['G']}')
    