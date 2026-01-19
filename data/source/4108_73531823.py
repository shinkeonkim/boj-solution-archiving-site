import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def solve():
  while 1:
    r, c = mii()
    
    if r == c == 0:
      break
    
    l = [input() for _ in range(r)]
    cnt = [[0] * c for _ in range(r)]
    
    
    
    for i in range(r):
      for j in range(c):
        if l[i][j] == '*':
          continue
        for d in range(8):
          ny = i + dy[d]
          nx = j + dx[d]
          
          if ny < 0 or nx < 0 or ny >= r or nx >= c:
            continue
          
          if l[ny][nx] == '*':
            cnt[i][j] += 1
    
    for i in range(r):
      for j in range(c):
        p(end=("*" if l[i][j] == '*' else str(cnt[i][j])))
      p()
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

