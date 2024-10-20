#!usr/bin/env python3

# function that calculates GC content of a DNA sequence
# takes in DNA sequence w/o spaces and no header
# returns % nucleotides that are G or C

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'

def gc_content(dna):
    gc = (dna.count('C') + dna.count('G'))
    return (gc / len(dna))

print(f'{gc_content(dna):.2%}')