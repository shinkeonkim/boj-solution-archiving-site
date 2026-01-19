import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  dx = [1,0,1,-1]
  dy = [0,1,1,1]
  
  n, m = mii()
  
  l = [mii() for _ in range(n)]
  cnt = [0, 0]
  
  for i in range(n):
    for j in range(m):
      if l[i][j] == 0:
        continue
        
      for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        
        
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
          continue
        
        if l[ny][nx] == 0:
          continue
        
        cnt[1] += 1
        if d < 2:
          cnt[0] += 1
  p(*cnt)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
