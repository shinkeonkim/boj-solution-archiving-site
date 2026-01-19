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

def f(a, b, c):
	for i in range(4):
		s = {a[i], b[i], c[i]}

		if len(s) == 1 or len(s) == 3:
			continue
		
		return False

	return True


def solve():
	l = []

	for i in range(4):
		l.extend(inp().split())

	cnt = 0
	for i in range(12):
		for j in range(i + 1, 12):
			for k in range(j + 1, 12):
				if f(l[i], l[j], l[k]):
					cnt += 1
					p(i + 1, j + 1, k + 1)

	if cnt == 0:
		p("no sets")


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
