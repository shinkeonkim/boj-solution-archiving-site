import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

a = mii()
b = mii()

A = B = 0

for i in a:
  for j in b:
    if i > j:
      A += 1
    if i < j:
      B += 1
print("{:.5f}".format(A / (A + B)))