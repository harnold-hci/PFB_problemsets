#!usr/val/bin python3
val = 90
if val > 0:
	print('positive')
	if val < 50:
		if (val % 2) == 0:
			print('it is an even number that is smaller than 50')
	elif val > 50:
		if (val % 3) == 0:
			print('it is larger than 50 and divisible by 3') 
	else:
		print('it is 50')
elif val < 0:
	print('negative')
elif val == 0:
	print('dude its zero')
