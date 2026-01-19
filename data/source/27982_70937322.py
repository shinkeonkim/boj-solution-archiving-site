import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b, c, n):
  return a * n * n + b * n + c

def solve():
  d = [0] * 220
  ans = 0
  n, m = mii()
  l = [mii() for _ in range(m)]
  
  for a, b, c in l:
    d[f(a, b, c, n)] = 1
    
  
  dx = [1,-1,0,0,0,0]
  dy = [0,0,1,-1,0,0]
  dz = [0,0,0,0,1,-1]

  for a, b, c  in l:
    cnt = 0
    for i in range(6):
      _a, _b, _c = a + dx[i], b + dy[i], c+ dz[i]
      
      if _a < 1 or _b < 1 or _c < 1 or _a > n or _b > n or _c > n:
        continue
      
      cnt += d[f(_a, _b, _c, n)]
    
    if cnt == 6:
      ans += 1
  
  p(ans)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
