import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = inp()
  
  crt = 0
  ans = set()
  
  for i in s:
    if '0' <= i <= '9':
      crt = crt * 10 + int(i)
    else:
      if crt > 0:
        ans.add(crt)
        crt = 0
  if crt > 0:
    ans.add(crt)
  
  p(len(ans))
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
