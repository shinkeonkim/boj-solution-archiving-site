import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
    sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def f(a):
	z = int("".join([str(9 - int(i)) for i in str(a)]))

	return a * z


def solve():
	n = ii()

	z = len(str(n)) # 자릿수 

	upto = 10 ** (z) // 2

	idx = min(upto, n)

	p(f(idx))

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()