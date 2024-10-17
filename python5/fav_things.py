#!usr/bin/env python3
import sys

book = 'Jitterbug Perfume'
song = 'Tom Petty - I Won\'t Back Down'
tree = 'Cedar'

fav_things = {'book': book, 'song': song, 'tree': tree}

print(fav_things)
print(fav_things['book'])
fav_thing = 'book'
print(fav_things[fav_thing])
print(fav_things['tree'])
fav_things['organism'] = 'mus'
print(fav_things.keys())

for key in fav_things:
	print(f'key: {key}, value: {fav_things[key]}')

print('insert key')

input = input()

fav_thing = input

print('insert key')
input2 = sys.argv[1]
fav_things[fav_thing] = input2
print(fav_things)
