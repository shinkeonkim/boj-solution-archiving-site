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
	MX = 1000001
	a = [0] * MX
	b = [0] * MX

	a[2] = 1
	a[4] = 2
	b[5] = 1

	for i in range(6, MX):
		if i % 2 == 0:
			a[i] = a[i // 2] + 1
		
		if i % 5 == 0:
			b[i] = b[i // 5] + 1
	
	for i in range(1, MX):
		a[i] += a[i - 1]
		b[i] += b[i - 1]
	
	tc = 1
	while True:
		n = ii()

		if n == 0:
			break
		
		p(f"Case #{tc}: {min(a[n], b[n])}")
		tc += 1



if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
