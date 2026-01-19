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

def f(a, base):
	ret = 0

	z = 1
	while a > 0:
		ret += (a % 10) * z
		z *= base
		a //= 10
	
	return ret

def g(s):
	ret = 2
	for i in s:
		if i == " ":
			continue
	
		ret = max(ret, int(i))
	return ret

def solve():
	s = input()

	mn = g(s)

	a, b, c = map(int, s.split())
	for base in range(mn + 1, 17):
		x = f(a, base)
		y = f(b, base)
		z = f(c, base)

		if x * y == z:
			p(base)
			return
	p(0)



if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()