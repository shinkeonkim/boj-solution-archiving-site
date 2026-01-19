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
	n, k = mii()
	l = mii()
	ans = 1e10

	for start in range(1, 2000):
		cnt = 0
		for j in range(n):
			ob = start + j * k

			diff = abs(ob - l[j])

			if diff > 0:
				cnt += 1
		
		ans = min(ans, cnt)

	p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()