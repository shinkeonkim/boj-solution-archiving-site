import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

def f(a, b):
  a = ord(a)
  b = ord(b)
  
  dis = abs(a - b)
  
  return min(dis, 26 - dis)
  
  

n = ii()
a = inp()
b = inp()
ans = 0

for i in range(n):
  ans += f(a[i], b[i])
print(ans)