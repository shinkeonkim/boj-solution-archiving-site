import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  a, b, c = mii()
  s = set()

  for i in range(c + 1):
    for j in range(0, c - i + 1):
      k = c - i - j
      
      if a + i <= b + j:
        continue
      
      s.add((a + i, b + j, k))
  print(len(s))
  
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
