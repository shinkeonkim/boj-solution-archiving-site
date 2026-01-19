import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  

def solve():
	n = ii()

	d = {}

	for i in range(n):
		a, b = inp().split()

		if a == "ChongChong":
			d[a] = True
		if b == "ChongChong":
			d[b] = True

		if d.get(a, False) or d.get(b, False):
			d[a] = d[b] = True
		
	p(sum(d.values()))



if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
