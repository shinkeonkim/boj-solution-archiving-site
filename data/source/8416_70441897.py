import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

def f(a, b):
  if b == 0:
    return 1
  if b == 1:
    return a % 10
  
  d = f(a, b // 2)
  
  return (d * d * a) % 10 if b % 2 else (d * d) % 10

a, b = mii()
print(f(a, b))