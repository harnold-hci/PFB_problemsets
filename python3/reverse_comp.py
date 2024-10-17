#!usr/var/bin python3

input = "5'ATGCAGGGGAAACATGATTCAGGAC 3'"

comp = ''
for base in input:
	if base == '5':
		comp = comp + '3'
	elif base == "\'" or base ==  " ":
		comp = comp + (base)
	elif base == 'A':
		comp = comp + ('T')
	elif base == 'T':
		comp = comp + ('A')
	elif base == 'C':
		comp = comp + ('G')
	elif base == 'G':
		comp = comp + ('C')
	elif base == '3':
		comp = comp + ('5')
	else:
		print('error! did not recognize base')

rev_comp = ''
for base in comp[::-1]:
	if base == "\'" or base == ' ':
		print(f'thinks {base} is a \' or space ')
		pass
	elif base.isdigit():
		print(f'thinks {base} is digit')
		rev_comp = rev_comp + ' ' + base + "\'"	
	else:
		print(f'thinks {base} is a base')
		rev_comp = rev_comp + base

print(f'Input: {input}')
print(f'Complement: {comp}')
print(f"comp answer: 3'TACGTCCCCTTTGTACTAAGTCCTG 5'")
print(f' rev_comp: {rev_comp}')
print(f"RevComp Ans: 5'GTCCTGAATCATGTTTCCCCTGCAT 3'")
