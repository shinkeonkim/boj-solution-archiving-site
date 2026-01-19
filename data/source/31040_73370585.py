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
  dx = [-2, -1, 1, 2, -2 , -1, 1, 2]
  dy = [1, 2, 2, 1, -1, -2, -2, -1]
  l = [input() for i in range(5)]
  flag = True
  for i in range(5):
    for j in range(5):
      if l[i][j] == '.':
        continue

      for d in range(8):
        ny = i + dy[d]
        nx = j + dx[d]

        if ny < 0 or nx < 0 or ny > 4 or nx > 4:
          continue

        if l[ny][nx] == 'k':
          flag = False
          break

  print("valid" if flag else "invalid")

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()