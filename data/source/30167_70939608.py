import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  l, r = mii()
  ans = -1
  
  for i in range(l, r+1):
    if len(str(i)) == len(set(list(str(i)))):
      ans = i
      break
  p(ans)
  
        
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()

    