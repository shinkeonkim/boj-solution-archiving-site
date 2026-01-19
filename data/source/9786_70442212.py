import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())


def f(a, b):
  return f(b, a % b) if b else a

for i in range(ii()):
  a, b = mii()
  d = f(a, b)
  
  print(a // d, b // d)