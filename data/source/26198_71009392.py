import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  d = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
  
  s = input()
  
  ans = 0
  for i in s:
    ans += d.get(i, 0)
  p(ans)
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
