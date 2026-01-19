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
	l = isplit()[::-1]
	VOWELS = "aeiouy"
	for i in l:
		s = i
		ret = ""
		for j in range(len(s)):
			if s[j] in VOWELS and j + 2 < len(s) and s[j + 1] not in VOWELS and s[j + 2] not in VOWELS:
				continue
			ret += s[j]
		
		ret = ret[::-1]
		p(ret, end = " ")


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
