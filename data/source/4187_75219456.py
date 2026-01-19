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
	k, w = mii()

	l = [inp() for _ in range(w)]

	ans = l[0]

	for i in range(1, w):
		crt = l[i]

		for j in range(k, 0, -1):
			if ans[-j:] == crt[:j]:
				ans += crt[j:]
				break
		else:
			ans += crt
	p(len(ans))





if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		ret = solve()
