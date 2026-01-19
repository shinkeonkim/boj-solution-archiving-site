import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  temp = -30
  oxy = 0
  ocean = 0
  
  for _ in range(n):
    k, a = input().split()
    a = int(a)
    
    if k == "temperature":
      temp += a
    elif k == "oxygen":
      oxy += a
    else:
      ocean += a
  
  if 9 <= ocean and 8 <= temp and 14 <= oxy:
    p("liveable")
  else:
    p("not liveable")
    
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
