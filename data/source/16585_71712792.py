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
  l = mii()
  
  k, s = input().split()
  k = int(k)
  
  if s == "left":
    A = sum(l[:k])
  else:
    A = sum(l[k-1:])
  
  k, s = input().split()
  k = int(k)
  
  if s == "left":
    B = l[:k].count(0)
  else:
    B = l[k-1:].count(0)
  print(A, B)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
