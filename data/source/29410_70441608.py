import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

def f(num, a, b):
  d = bin(num)[2:]
  return d.count("0") * a + d.count("1") * b

N, a, b = mii()
ans = 0

for _ in range(N):
  k, *l = mii()
  for i in l:
    ans += f(i, a, b)
print(ans)