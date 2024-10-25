#!usr/bin/env python3
from Bio import SeqIO
import Bio.SeqUtils

ifh = '/Users/pfb2024/pfb2024/files/Python_08.fasta'

total_seqs = 0
total_nts = 0
lowest = ''
longest = ''
all_nts = ''
gc_high = 0
gc_low = 100

for seq_record in SeqIO.parse(ifh, 'fasta'):
    # total number of sequences
    total_seqs += 1
    # total number of nucleotides
    total_nts += (len(seq_record.seq))
    all_nts = all_nts + seq_record.seq
    # shortest sequence length
    if not lowest:
        lowest = seq_record.seq
    if len(seq_record.seq) < len(lowest):
        lowest = seq_record.seq
    # longest sequence length
    if not longest:
        longest = seq_record.seq
    if len(seq_record.seq) > len(longest):
        longest = seq_record.seq
    # highest GC content
    temp_high = Bio.SeqUtils.gc_fraction(seq_record.seq)
    if gc_high < temp_high:
        gc_high = temp_high
    # lowest GC content
    temp_low = Bio.SeqUtils.gc_fraction(seq_record.seq)
    if gc_low > temp_low:
        gc_low = temp_low

print('total seqs:', total_seqs)
print('total nucleotides:', total_nts)
# average length of sequences:
print(f'average length of sequences: {total_nts/total_seqs:.2f}')
# shortest sequence
print('shortest seq:', len(lowest))
# longest sequence
print('longest seq:', len(longest))
# average GC content:
print(f'gc content: {Bio.SeqUtils.gc_fraction(all_nts):.2%}')
# highest GC content:
print(f'highest GC content: {gc_high:.2%}')
# lowest GC content:
print(f'lowest GC content: {gc_low:.2%}')