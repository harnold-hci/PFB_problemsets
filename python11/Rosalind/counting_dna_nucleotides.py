'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective 
number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

count = {}
for nt in dna:
    print('nt', nt)
    print('countNT', count[nt])
    if not count[nt]:
        count[nt] = 1
    count[nt] += 1
print(count['A'], count['C'], count['G'], count['T'])