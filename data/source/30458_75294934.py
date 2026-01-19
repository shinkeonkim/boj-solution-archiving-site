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
	s = inp()

	z = n // 2

	a = s[:z]
	b = s[-z:]


	d = {}

	for i in a+b:
		d[i] = d.get(i, 0) + 1

	for i in d.values():
		if i % 2:
			p("No")
			return
	p("Yes")

if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
