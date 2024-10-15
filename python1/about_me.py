#!/usr/bin/env python3
import sys
print("My name: Henry")
print( "My favorite color: chartruse")
activity = 'skiing'
print(f'My favorite activity: {activity:>10}')
print('My favorite animal: gila monster')
name = sys.argv[1]
color = sys.argv[2]
activity2 = sys.argv[3]
animal = sys.argv[4]
print(name, color, activity2, animal)
