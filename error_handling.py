#!/usr/bin/env python
while True:
    reply = input('Enter a number: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except: 
        print('Bad! ' * 8)
    else:
        print(num ** 2)
print('Bye!')
