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

	z = [l]
	for _ in range(4 - n):
		z2 = []
		for ar in z:
			for i in range(1, 7):
				ar2 = ar[::] + [i]
				z2.append(ar2)
		z = z2
	
	diff = 0

	for i in z:
		if len(set(i)) != len(i):
			diff += 1
	
	p(len(z) - diff, diff)


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()