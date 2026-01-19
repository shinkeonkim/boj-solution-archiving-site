import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(n):
  cnt = 0
  for i in range(1, n):
    if n % i == 0:
      cnt += 1
  return cnt

def solve():
  n, k = mii()
  
  for i in range(n):
    for j in range(n):
      d = i * n + j + 1
      
      if f(d) < k:
        p(end="*")
      else:
        p(end=".")
    p()
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

