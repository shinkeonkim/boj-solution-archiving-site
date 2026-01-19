import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m = mii()
  names = [input() for _ in range(n)]
  ans = ""
  for i in range(0, m):
    d = {}
    for name in names:
      d[name[i]] = d.get(name[i], 0) + 1
    
    l = sorted(list(d.items()), key = lambda t : (-t[1], t[0]))
    
    ans += l[0][0]
  
  p(ans)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

