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
  n = ii() // (52 * 7)
  ans = []

  for x in range(1, 101):
    left = n - x
    if left <= 0:
      continue
    
    if left % 3 > 0:
      continue
    
    k = left // 3
    
    ans = [x, k]

  print(*ans, sep="\n")
    
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()
   