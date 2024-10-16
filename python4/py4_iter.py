#!usr/var/bin python3
import sys

lis = [101,2,15,22,95,33,2,27,72,15,52]

sort_list = sorted(lis)
print(sort_list)

even = 0
odd = 0
for oje in sort_list:
	print(oje)
	if oje % 2 == 0:
		even += oje
	else:
		odd += oje
print(f'Sum of even numbers: {even}')
print(f'Sum of odd numbers: {odd}')

for thing in lis:
	if thing % 2 == 0:
		print(thing)
