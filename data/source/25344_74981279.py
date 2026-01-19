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

def solve():
	n = ii() - 2
	l = mii()

	ret = l[0]
	for i in range(1, n):
		ret = ret * l[i] // gcd(ret, l[i])
	
	p(ret)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
