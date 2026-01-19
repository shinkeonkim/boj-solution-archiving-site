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
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
	n = ii()
	
	d = {}

	for _ in range(n):
		a, b = mii()
		d[a] = b
	
	m = ii()

	for _ in range(m):
		k, *l = mii()

		ans = []
		for i in l:
			ret = d.get(i, -1)

			if ret == -1:
				p("YOU DIED")
				break
			ans.append(ret)
		else:
			p(*ans)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
