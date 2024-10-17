#!usr/var/bin python3
import random

# initializing my freaking variables
seq = 'CATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCT'
n = len(seq)

# doing the swap for as many times as the sequence is long
for i in seq:
	# generate random numbers in a tuple
	rand_tuple = (random.randrange(n), random.randrange(n))
	a = min(rand_tuple)
	b = max(rand_tuple)
	# print tests	
	print(f'seq {seq}')
	print(f'a: {a}, b: {b}')
	#exchange the letters at a and b
	base_a = seq[a]
	base_b = seq[b]
	seq = seq[:a] + base_b + seq[a + 1:]
	print(seq)
	seq = seq[:b] + base_a + seq[b + 1:]
	print(seq)
