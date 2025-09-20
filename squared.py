#!/usr/bin/env python
while True:
    reply = input('Enter number: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad! ' *8)
    else:
        print(int(reply) ** 2)
print('Bye!')
