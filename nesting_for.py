#!/usr/bin/env python
items = ['aaa', 111, 5, 7, 'bbb']
tests = [5, 7, 'ccc']

for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')
            break
        else:
            print(key, 'not found')
