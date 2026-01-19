import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  k = "aeiouy"
  k2 = "AEIOUY"

  s = inp()
  
  for i in s:
    if i in k:
      print(end=k[(k.index(i) + 1) % 6])
    elif i in k2:
      print(end=k2[(k2.index(i) + 1) % 6])
    else:
      print(end=i)
  print()
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(tc):
    solve()
    