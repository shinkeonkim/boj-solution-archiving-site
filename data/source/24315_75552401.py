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
	a1, a0 = mii()
	c1, c2 = mii()
	n0 = ii()

	INF = 1e30

	A = c1 * n0  <= a1 * n0 + a0 <= c2 * n0
	B = c1 * INF  <= a1 * INF + a0 <= c2 * INF

	p(int(A and B))

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()