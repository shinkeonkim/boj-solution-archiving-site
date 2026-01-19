import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def get_dis(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve():
	n = ii()

	COMMON = mii()

	l = [mii() for _ in range(n)]
	ans = 0

	for i in range(n):
		crt = l[i]

		power = max(0, COMMON[2] - get_dis(COMMON, crt))

		for j in range(n):
			minus = l[j]

			dis = get_dis(crt, minus)
			power -= max(0, minus[2] - dis)

		ans = max(ans, power)
	
	p("IMPOSSIBLE" if ans <= 0 else ans)
			


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()