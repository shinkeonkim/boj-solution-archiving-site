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
	n = ii()
	st = 1
	en = n

	ans = []
	while st <= en:
		if st == en:
			ans.append(st)
			st += 1
			en -= 1
		else:
			ans.extend([en, st])
			en -= 1
			st += 1
	p(*ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
