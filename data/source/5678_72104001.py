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
    n = ii()
    if n == 0:
      break
    
    mark = mii()
    leti = mii()
    
    A = sum(mark)
    B = sum(leti)
    
    for i in range(2, n):
      a = (mark[i - 2] == mark[i - 1] == mark[i])
      b = (leti[i - 2] == leti[i - 1] == leti[i])
      
      if a and b:
        break
      if a:
        A += 30
        break
      if b:
        B += 30
        break
        
    if A > B:
      p("M")
    elif A < B:
      p("L")
    else:
      p("T")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
