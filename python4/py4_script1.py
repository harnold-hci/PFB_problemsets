#!usr/var/bin python3
import sys

taxa_String = 'sapiens : erectus : neanderthalensis'
print(f'string: {taxa_String}')

taxa_list = taxa_String.split(':')
print(f'taxa list: {taxa_list}')
print(f'taxa[1]: {taxa_list[1]}')

print(f'taxa_string type: {type(taxa_String)}')
print(f'taxa_list type: {type(taxa_list)}')

s_list = sorted(taxa_list)
print(s_list)

s_v2 = sorted(taxa_list, key=len)
print('sorted_v2', s_v2)
