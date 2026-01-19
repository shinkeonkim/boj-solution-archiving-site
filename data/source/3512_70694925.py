import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

def f(a):
  return [int(a[0]), a[1]]

n, c = mii()
l = [f(input().split()) for i in range(n)]

s = 0
b = 0
o = 0
for i in l:
  s += i[0]
  
  if i[1] == 'bedroom':
    b += i[0]
  if i[1] == 'balcony':
    o += i[0]
    
print(s)
print(b)
print(s * c - o * c / 2)