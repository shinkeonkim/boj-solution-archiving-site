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

def f(s, k):
	ret = ""

	for i in s:
		ret += chr((ord(i) - 97 + k + 26) % 26 + 97)

	return ret

def solve():
	s = inp()
	n = ii()

	l = [inp() for _ in range(n)]

	for z in range(26):
		s2 = f(s, z)

		for i in l:
			if i in s2:
				p(s2)
				return


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()