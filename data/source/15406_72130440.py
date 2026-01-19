import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  cost = 0
  while 1:
    s = inp()
    if s == "TOTAL":
      break
      
    n, k = mii()
    cost += n * k
  
  total = ii()
  
  if total <= cost:
    p("PAY")
  else:
    p("PROTEST")
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
