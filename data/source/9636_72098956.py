import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  cnt = 0
  X = Y = 0

  for d in s:
    if d == "?":
      cnt += 1

    elif d == "R":
      X += 1
    elif d == "L":
      X -= 1
    elif d == "U":
      Y += 1
    else:
      Y -= 1
    
  print(X - cnt, Y - cnt, X + cnt, Y + cnt)
      
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
