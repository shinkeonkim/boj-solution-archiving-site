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


def f(n):
	return n * (n + 1) * 2


def solve():
	n, k = mii()

	start = max(0, n - k - 1)
	end = n

	p(f(end) - f(start))


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()