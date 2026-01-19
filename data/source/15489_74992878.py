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
	d = [[0] * 40 for _ in range(40)]

	d[0][0] = 1
	for i in range(1, 31):
		for j in range(i + 1):
			s = max(0, j - 1)
			d[i][j] = sum(d[i - 1][s:j + 1])
	
	r, c, w = mii()
	r -= 1
	c -= 1
	ans = 0
	for i in range(w):
		for j in range(i + 1):
			y = r + i
			x = c + j

			ans += d[y][x]
	p(ans)
		

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
