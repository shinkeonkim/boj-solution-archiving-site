import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
l = [inp() for i in range(n)]
d = [[0] * 20 for _ in range(10)]

for i in l:
  a = ord(i[0]) - 65
  b = int(i[1:]) - 1
  d[a][b] = 1

for i in range(10):
  for j in range(20):
    print("." if d[i][j] == 0 else "o", end="")
  print()