import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

h, l, a, b = mii()

print("YES" if (h * 2 >= a and l >= b) or (h * 2 >= b and l >= a) else "NO")