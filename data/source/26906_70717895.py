import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


n = ii()
d = {}

for i in range(n):
  v, k = input().split()
  d[k] = v

s = input()
ans = ""

for i in range(0, len(s), 4):
  ans += d.get(s[i:i+4], "?")
print(ans)