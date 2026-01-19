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

  k = ""

  for i in s:
    if i in "aeiou":
      k += i

  return "S" if k == k[::-1] else "N"

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)