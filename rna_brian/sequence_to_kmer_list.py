#!usr/bin/env python3

# Write a python script to extract all kmers of specified length from nucleotide sequence
# usage: ./sequence_to_kmer_list.py sequence kmer_length

import argparse
import sys

def sequence_to_kmer_list(seq, kmer_length):
    output_list = []
    for i in range(len(seq)-kmer_length+1):
        output_list.append(seq[i:i+kmer_length])
    return output_list

def main():
    # setting up argparse to read in from command line
    parser = argparse.ArgumentParser(description='function returning list of kmers from sequence')
    parser.add_argument('sequence', help = 'sequence to iterate over')
    parser.add_argument('kmer_len', type=int, help='number of bases per kmer')
    args = parser.parse_args()
    
    # assigning variables from command line
    sequence = args.sequence
    kmer_len = args.kmer_len

    usage = '\n\n\tusage: {} sequence kmer_length\n\n\n'.format(sys.argv[0])
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)
    
    # run the defined function, print length to be shown
    kmer_list = sequence_to_kmer_list(sequence, kmer_len)
    print(kmer_list)

    sys.exit(0)

if __name__ == '__main__':
    main()