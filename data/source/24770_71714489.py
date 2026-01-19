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
    n, m = mii()

    if n == m == 0:
      break
    
    l = sorted([mii() for _ in range(n)])
    
    ans = [1, 100000000]
    for a, b in l:
      if a > m:
        break
        
      if ans[1] * a >= b * ans[0]:   
        ans = [a, b]
    
    if ans == [1, 100000000]:
      print("No suitable tickets offered")
    else:
      print(f"Buy {ans[0]} tickets for ${ans[1]}")
      
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
