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
  n, q = mii()
  lengths = [ii() for _ in range(n)]
  queries = [ii() for _ in range(q)]
  
  song = []
  for i in range(n):
    song.extend([i + 1] * lengths[i])
  
  for i in queries:
    p(song[i])
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()
   