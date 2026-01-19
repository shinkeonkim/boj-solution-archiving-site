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

def f(a):
	return [[a[0], a[0] + a[3]], [a[1], a[1] + a[2]]]

def dup(a, b):
	A = max(a[0][0], b[0][0]) < min(a[0][1], b[0][1])
	B = max(a[1][0], b[1][0]) < min(a[1][1], b[1][1])
	
	return A and B

def solve():
	while 1:
		n = ii()

		if n == 0:
			break
		
		l = [f(mii()) for _ in range(n)]
		chk = [False] * n
		
		for i in range(n):
			for j in range(i + 1, n):
				if dup(l[i], l[j]):
					chk[i] = chk[j] = True

		p(chk.count(True))


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
