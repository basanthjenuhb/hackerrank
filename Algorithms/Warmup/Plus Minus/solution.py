#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos,zero,neg=0.0,0.0,0.0
for x in arr:
    if x < 0:neg+=1
    elif x == 0: zero+=1
    else: pos+=1
print pos/n
print neg/n
print zero/n
