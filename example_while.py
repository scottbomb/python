#!/usr/bin/env python
while(True):
    answer = input("Type an integer: ")
    try:
        answer = int(answer)
    except:
        print("Not an integer!")
    else:
        print("Excellent!")
