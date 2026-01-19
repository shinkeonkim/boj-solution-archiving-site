import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = mii()
one = l.count(1)

need = n // 2 + int(n % 2)
print(max(0, need - one))