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
	d = [INF for _ in range(60)]
	d[0] = 0
	d[3] = 1
	d[5] = 1

	n = ii()

	for i in range(6, 60):
		d[i] = 1 + min(d[i - 3], d[i - 5])
	
	if n in [1, 2, 4, 7]:
		p(-1)
	else:
		if n < 60:
			p(d[n])
		else:
			p(d[n % 15 + 15] + (n // 15 - 1) * 3)



if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
