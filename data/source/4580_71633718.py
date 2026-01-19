import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    l = mii()
    
    if len(l) == 1:
      break
    
    n, *l = l

    l = [0] + l
    
    for i in range(1, n + 1):
      print((str(i) + " ") * (l[i] - l[i - 1]), end = "")
    print()
    

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
