import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def solve():
  w, h = mii()
  
  l = [input() for _ in range(h)]
  
  ans = 0
  dy = [0,0,1,-1]
  dx = [1,-1,0,0]
  
  for i in range(h):
    for j in range(w):
      for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
          continue
          
        if l[i][j] != l[ny][nx]:
          ans += 1
  print(ans // 2)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    