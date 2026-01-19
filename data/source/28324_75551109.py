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
	l = mii()

	for i in range(n):
		v = l[i]
		left_dis = n - i

		l[i] = min(v, left_dis)


	prev = l[-1]
	ans = prev

	for i in range(n - 2, -1, -1):
		crt = l[i]

		if crt <= prev:
			ans += crt
			prev = crt
		else:
			ans += prev + 1
			prev = prev + 1

	p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()