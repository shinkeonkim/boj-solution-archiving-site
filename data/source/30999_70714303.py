import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


n, m = mii()
l = [input() for _ in range(n)]
ans = 0

for i in l:
  k = i.count("O")
  
  if m < k * 2:
    ans += 1
print(ans)