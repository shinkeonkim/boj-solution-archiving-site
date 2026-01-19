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


def solve():
	s = inp()

	ret = ""
	for i in range(len(s)):
		if (s[i] == "-" or s[i] == ":")and i != 0 and ret[-1] != BLANK:
			ret += BLANK
		
		ret += s[i]
		if (s[i] == "-" or s[i] == ":") and i + 1 < len(s) and s[i + 1] != BLANK:
			ret += BLANK
	p(ret)


if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		ret = solve()
