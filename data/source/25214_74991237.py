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

INF = 1e19

def solve():
	ans = 0
	n = ii()
	l = mii()

	mn = l[0]
	p(0, end = " ")
	for i in range(1, n):
		crt = l[i]
		ans = max(ans, crt - mn)
		mn = min(mn, crt)
	
		p(ans, end = " ")




if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
