import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  m, n = mii()
  l = [[*map(int, list(input()))] for _ in range(m)]
  
  dy = [0,0,1,-1]
  dx = [1,-1,0,0]
  ans = []

  for i in range(m):
    for j in range(n):
      c = 0
      sm = 0

      for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        
        if ny < 0 or nx < 0 or ny >= m or nx >= n:
          continue
      
        c += 1
        sm += abs(l[ny][nx] - l[i][j])
      
      ans.append(sm * (12 // c))
  
  p(f"{sum(ans) / 12:.4f}")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()