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
	n = ii()
	names = [inp() for _ in range(n)]

	chk = [False] * n

	for _ in range(ii()):
		l = isplit()

		for i in l:
			for idx in range(n):
				if i == names[idx]:
					chk[idx] = True
	
	for idx in range(n):
		p(f"{names[idx]} is {'present' if chk[idx] else 'absent'}")
			



if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		p(f"Test set {t}:")
		ret = solve()
		p()
