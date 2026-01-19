import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  z = [
    [-1, -1, '\\'],
    [-1, 0, '|'],
    [-1, 1, '/'],
    [0, -1, '-'],
    [0, 1, '-'],
    [1, -1, '/'],
    [1, 0, '|'],
    [1, 1, '\\'],
  ]
  
  n, m = mii()
  l = [input() for _ in range(n)]
  ans = 0
  for i in range(n):
    for j in range(m):
      if l[i][j] == '+':
        cnt = 0
        for k in range(1, max(n, m)):
          chk = True
          for d in range(8):
            ny = i + z[d][0] * k
            nx = j + z[d][1] * k
            
            
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
              chk = False
              break
            if l[ny][nx] != z[d][2]:
              chk = False
              break
          if chk:
            cnt += 1
          else:
            break
        ans = max(ans, cnt)
  p(ans)
        
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
