import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  cow = mii()
  bee = mii()
  
  n = ii()
  
  cow_s = [0, cow[0]]
  bee_s = [0, bee[0]]
  
  k = cow[0]
  for i in range(100):
    k -= cow[1]
    k = max(k, 0)
    cow_s.append(cow_s[-1] + k)
  
  k = bee[0]
  for i in range(100):
    k -= bee[1]
    k = max(k, 0)
    bee_s.append(bee_s[-1] + k)
  
  ans = 0
  for _ in range(n):
    a, b = mii()
    
    ans += max(cow_s[a], bee_s[b])
  
  p(ans)  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

