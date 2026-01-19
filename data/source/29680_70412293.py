import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

H, W, w1, w2 = mfi()
print(((w1 + w2) * H) + (W * w1) + (W * sqrt(H * H + (w2 - w1) ** 2)))