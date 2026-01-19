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

MOD = 1000000007

def f(a, k):
	if k == 1:
		return a

	z = f(a, k // 2)

	if k % 2 == 0:
		return (z * z) % MOD

	return (z * z * a) % MOD


def solve():
	n, m = mii()

	A = f(m, n)
	B = f(m - 1, n)

	p((A + MOD - B) % MOD)



if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
