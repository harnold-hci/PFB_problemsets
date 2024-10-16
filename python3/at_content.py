#!usr/var/bin python3
import sys

input = sys.argv[1]
dna = input.upper()

a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')

at_count = a_count + t_count
gc_count = g_count + c_count

total_count = len(dna)

at_content = at_count / total_count
gc_content = gc_count / total_count


print(f'A count: {a_count}')
print(f'T count: {t_count}')
print(f'AT content: {at_content:.3} or {at_content:.1%}')


print(f'G count: {g_count}')
print(f'C count: {c_count}')
print(f'GC content: {gc_content:.3} or {gc_content:.1%}')
