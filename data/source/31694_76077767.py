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
	algosia = mii()
	bajtek = mii()

	A = [0] * 11
	B = [0] * 11

	x = y = 0
	for i in algosia:
		A[10 - i] -= 1
		x += i
	for j in bajtek:
		B[10 - j] -= 1
		y += j
	
	A = [-x] + A
	B = [-y] + B
	if A == B:
		p("remis")
	elif A < B:
		p("Algosia")
	else:
		p("Bajtek")

if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
