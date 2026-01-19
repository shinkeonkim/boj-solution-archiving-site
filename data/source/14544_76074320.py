import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
	sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print


def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def solve():
	n, m = mii()

	names = [inp() for _ in range(n)]
	cnt = {}

	for name in names:
		cnt[name] = 0
	
	for _ in range(m):
		a, b, c = isplit()

		b = int(b)
		cnt[a] += b
	
	mx = max(cnt.values())

	if [*cnt.values()].count(mx) > 1:
		p("THERE IS A DILEMMA")
	else:
		for k, v in cnt.items():
			if v == mx:
				p(f"THE WINNER IS {k} {v}")


if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		p(end=f"VOTE {t}: ")
		ret = solve()
	