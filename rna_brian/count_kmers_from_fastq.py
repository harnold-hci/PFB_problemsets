#!usr/bin/env python3

# count all kmers in all sequences
# usage: ./count_kmers_from_fastq.py filename.fastq kmer_length num_top_kmers_show

import argparse
import sys
import math
from sequence_to_kmer_list import sequence_to_kmer_list
from fastq_file_to_sequence_list import seq_list_from_fastq_file


def count_kmers(test_list):
    kmer_count_dict = {}
    for kmer in test_list:
        if kmer not in kmer_count_dict.keys():
            kmer_count_dict[kmer] = 1
        else:
            kmer_count_dict[kmer] += 1
    return(kmer_count_dict)

def calc_entropy(kmer):
    base_count = {}
    total_base_count = 0
    base_fractions = {}
    # count bases in kmer
    for base in kmer:
        if base not in base_count:
            base_count[base] = 1
            total_base_count += 1
        else:
            base_count[base] += 1
            total_base_count += 1
    for nt in base_count.keys():
        base_fractions[nt] = base_count[nt] / total_base_count
    ent = 0.0
    for nt in base_fractions:
        frac = base_fractions[nt]
        ent = ent + (frac * math.log2(frac))
    ent = ent * -1
    return(ent)

def main():
    # setting up argparse to read in from command line
    parser = argparse.ArgumentParser(description='function counting kmers from sequence')
    parser.add_argument('filename', help = 'fastq file to import')
    parser.add_argument('kmer_len', type=int, help='number of bases per kmer')
    parser.add_argument('num_top_kmers_show', type=int, help='number of top kmers to show')
    args = parser.parse_args()
    
    # assigning variables from command line
    filename = args.filename
    kmer_len = args.kmer_len
    show = args.num_top_kmers_show

    usage = '\n\n\tusage: {} filename kmer_length num_to_show\n\n\n'.format(sys.argv[0])
    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)
    
    all_kmers = []
    # create a list of all the sequences in the fastq file
    seq_list = seq_list_from_fastq_file(filename)
    # append all kmers from the entire fastq file to a long list
    for seq in seq_list:
        temp_kmers = sequence_to_kmer_list(seq, kmer_len)
        for kmer in temp_kmers:
            all_kmers.append(kmer)
    # create a dictionary that counts the occurance of each kmer
    kmer_dict = count_kmers(all_kmers)
    # create a list of all the kmers. Duplicates dropped.
    unique_kmers = list(set(all_kmers))
    # sort each kmer by how many times it appears, descending order
    unique_kmers_sorted = sorted(unique_kmers, key=lambda x: kmer_dict[x], reverse=True)
    # print the inputed number of kmers to show
    for kmer in unique_kmers_sorted[:show]:
        print(kmer, kmer_dict[kmer], calc_entropy(kmer))    
    sys.exit(0)

if __name__ == '__main__':
    main()