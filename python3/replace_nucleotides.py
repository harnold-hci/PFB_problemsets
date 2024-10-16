#!usr/var/bin python3
import sys

input = sys.argv[1]
print('input:', input)
dna = input.upper()

#pos_control = 'AUGCAUGC'

ans = dna.replace('T','U')

#print('positive control:', pos_control)
print('generated result:', ans)
#print(pos_control ==  ans)
