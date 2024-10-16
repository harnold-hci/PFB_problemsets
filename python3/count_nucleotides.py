#!usr/var/bin python3
import sys

input = sys.argv[1]

dna = input.upper()
A = dna.count('A')
T = dna.count('T') 
G = dna.count('G')
C = dna.count('C')
print(f'A: {A}, T: {T}, G: {G}, C: {C}')
