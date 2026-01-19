import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


for _ in range(ii()):
  n = ii()
  s = input()
  
  d = {
    'S': (1, 0),
    'N': (-1, 0),
    'W': (0, 1),
    'E': (0, -1),
  }
  
  ans = [0, 0]
  for i in s:
    ans[0] += d[i][0]
    ans[1] += d[i][1]
  
  print(abs(ans[0]) + abs(ans[1]))