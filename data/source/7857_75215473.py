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

def get_prefix(a, b):
	ret = 0
	for i in range(min(len(a), len(b))):
		if a[i] == b[i]:
			ret += 1
		else:
			return ret
	return ret

def solve():
	n = ii()

	l = [inp() for _ in range(n)]

	ans = len(l[0])

	for i in range(1, n):
		k = get_prefix(l[i - 1], l[i])

		ans += 1 + len(l[i]) - k
	p(ans)

if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()