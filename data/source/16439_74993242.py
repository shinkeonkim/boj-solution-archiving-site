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
	n, m = mii()
	l = [mii() for _ in range(n)]
	ans = 0
	for i in range(m):
		for j in range(i + 1, m):
			for k in range(j + 1, m):
				idx = [i, j, k]
				
				ret = 0
				for per in range(n):
					mx = 0
					for t in idx:
						mx = max(mx, l[per][t])
					
					ret += mx
				
				ans = max(ans, ret)
	p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
