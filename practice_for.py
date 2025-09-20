#!/usr/bin/env python
# examples of for use

print('simplest for loop')
test = ['a', 'b', 'c', 'd']
for x in test:
    print(x)

print('for loop with a break in it')
for x in test:
    if x == "c": break
    print(x)

print('for loop with continue')
for x in test:
    if x == "c": continue
    print(x)

print('iterate through a dictionary')
testDict={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for x in testDict:
    print(x, "=>", testDict[x])

print('\nBye!')

