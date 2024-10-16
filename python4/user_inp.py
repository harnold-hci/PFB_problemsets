#!usr/var/bin python3
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

for i in range(min, max+1):
	if i % 2 != 0:
		print(i)

