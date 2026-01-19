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
	m = ii()
	d = {}
	for _ in range(m):
		query = mii()

		if query[0] == 1:
			d[query[2]] = query[1]
			# x번에 w 볼을 넣는다.
		else:
			p(d[query[1]])
			# w 볼이 있는 위치
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
