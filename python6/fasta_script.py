#!usr/bin/env python3

# parse a .fasta file into a dictionary.
# should be key (gene?) and value (bases)

# format: >xxx \n AAAGTCCCGGTA

with open('/Users/pfb2024/pfb2024/files/Python_06.fasta') as f:
	fast_dict = {}
	count = 0
	temp_key = ''
	temp_val = ''
	for line in f:
		line = line.rstrip()
		# see if this is a header or sequence
		if line.startswith('>'):
			# see if temp_key is empty. this avoids fencepost problem. only if full
			# will it assign the previous sequence to a key and reset the value
			if temp_key:
				fast_dict[temp_key] = temp_val
				temp_val = ''
			# sets the temp key as the seq, getting rid of the >
			temp_key = line.lstrip('>')
			# fencepost!!!!!
		else:
			# if it's actual sequences, concatenates the sequences until the next > is reached
			temp_val = temp_val + line 
	# fencepost
	fast_dict[temp_key] = temp_val
	temp_val = ''
print(fast_dict)

answer = { 'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' , 'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' , 'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' , 'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }

print(fast_dict == answer)