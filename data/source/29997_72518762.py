import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = list(input())
  k = ii()
  l = [[] for _ in range(k)]
  
  n = len(s)
  for i in range(n):
    l[i % k].append(s[i])
    
  for i in range(k):
    l[i].sort()
  
  ans = ""
  
  for i in range(n):
    a = i % k
    b = i // k
    ans += l[a][b]
  
  p(ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   