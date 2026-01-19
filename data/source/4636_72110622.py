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
    
    if n == -1:
      break
      
    l = [input().split() for _ in range(n)]
    
    vol = []
    ans = []
    for a, b, c, d in l:
      vol.append(int(a) * int(b) * int(c))
    
    average = sum(vol) // n

    for a, b, c, d in l:
      v = int(a) * int(b) * int(c)
      
      if v != average:
        ans.append([d, v])
    
    if ans[1][1] > ans[0][1]:
      ans[1], ans[0] = ans[0], ans[1]
      
    print(f"{ans[0][0]} took clay from {ans[1][0]}.")
        
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
