#!usr/var/bin python3
import sys

input = sys.argv[1]
pos1 = int(sys.argv[2])
pos2 = int(sys.argv[3])

dna = input.upper()

print(f'DNA extraction from position {pos1} to position {pos2}:')
print(dna[(pos1-1):pos2])
