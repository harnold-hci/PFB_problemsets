#!usr/bin/env python3

# function that takes DNA seq w/o spaces and no header
# returns reverse complement

dna = 'ATCG'

def rev_comp(dna):
    dna2 = dna.replace('A', 't')
    dna2 = dna2.replace('T', 'a')
    dna2 = dna2.replace('C', 'g')
    dna2 = dna2.replace('G', 'c')
    dna2 = dna2[::-1]
    dna2 = dna2.upper()
    return dna2
print(rev_comp(dna))