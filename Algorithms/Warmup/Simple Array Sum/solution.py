#!/bin/python

n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
sum = 0
for x in arr:
    sum+=x
print(sum)
