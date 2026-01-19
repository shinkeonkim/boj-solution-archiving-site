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


def f(num):
	return len(set(str(num)) - set("58")) == 0


def solve():
	inp()
	A = set(mii())

	inp()
	B = set(mii())

	inp()
	C = set(mii())

	ans = set()
	for i in A:
		for j in B:
			for k in C:
				if f(i + j + k):
					ans.add(i + j + k)

	p(len(ans))	


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()