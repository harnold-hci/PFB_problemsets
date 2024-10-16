#!usr/var/bin python3
import sys

input = sys.argv[1]
pos1 = int(sys.argv[2])
pos2 = int(sys.argv[3])

dna = input.upper()

extract = dna[(pos1-1):pos2]

print(f'DNA extraction from position {pos1} to position {pos2}:')
print(extract)

g_count = extract.count('G')
print(f'G count: {g_count}')




