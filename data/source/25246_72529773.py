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

  idx = -1

  for i in range(len(s) - 1, - 1, -1):
    if s[i] in "aeiouAEIOU":
      idx = i
      break
  print(s[:idx+1]+"ntry")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
