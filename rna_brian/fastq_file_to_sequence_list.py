#!usr/bin/env python3

# Write a python script that retrieves a list of all read sequences from a fastq file.
# usage: fastq_file_to_sequence_list.py reads.fq 10

import argparse
import sys

def seq_list_from_fastq_file(fastq_filename):
    seq_list = []
    with open(fastq_filename) as ifh:
        count = -2
        for line in ifh:
            count += 1
            if count % 4 == 0:
                line = line.rstrip()
                seq_list.append(line)
    return(seq_list)

def main():
  
    # setting up argparse to read in from command line
    parser = argparse.ArgumentParser(description='function formating fastq sequence into list')
    parser.add_argument('file', help = 'path to input fasta filename')
    parser.add_argument('show_length', type=int, help='number of sequences to show')
    args = parser.parse_args()
    
    # assigning variables from command line
    fastq_filename = args.file
    show = args.show_length

    usage = '\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n'.format(fastq_filename)
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)
    
    # run the defined function, print length to be shown
    seq_list = seq_list_from_fastq_file(fastq_filename)
    print(seq_list[:show])

    sys.exit(0)

if __name__ == '__main__':
    main()