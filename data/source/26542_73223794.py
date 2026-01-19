import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(s):
  return 1 if s == '#' else 0

def solve():
  n = ii()
  l = [input() for _ in range(n)]
  
  ans = -1
  
  D = [[0] * (n + 1) for _ in range(n + 1)]
  for i in range(n):
    for j in range(n):
      if i == 0 and j == 0:
        D[i+1][j+1] = f(l[i][j])
      elif i == 0:
        D[i+1][j+1] = D[i+1][j] + f(l[i][j])
      elif j == 0:
        D[i+1][j+1] = D[i][j+1] + f(l[i][j])
      else:
        D[i+1][j+1] = D[i][j+1] + D[i+1][j] - D[i][j] + f(l[i][j])
  
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      for d in range(0, n + 1):
        s = (i, j)
        e = (i+d, j+d)
        
        if e[0] > n or e[1] > n:
          continue
        
        k = D[e[0]][e[1]] - D[e[0]][s[1]-1] - D[s[0]-1][e[1]] + D[s[0]-1][s[1]-1]
        
        if k == 0:
          ans = max(ans, d)
  p((ans + 1) ** 2)
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
