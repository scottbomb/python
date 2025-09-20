#!/usr/bin/env python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print matrix
print matrix[1]
column = [x[1] + 1 for x in matrix]
print column
column2 = [x[2] + 2 for x in matrix]
print column2
column3 = [x[0] + 3 for x in matrix]
print column3
all = column + column2 + column3
print all
evens = [[x] for x in all if x % 2 == 0]
odds = [[x] for x in all if x % 2 == 1]
print evens
print odds
all = odds + evens
print all
diag = [matrix[i][i] for i in  [0,1,2]]
print diag
diag = [matrix[i][i] for i in  [2,1,0]]
print diag
all.sort()
print all
