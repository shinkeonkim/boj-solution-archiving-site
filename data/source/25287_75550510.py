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
	l = mii()

	
	crt = l[n - 1]
	alter = n - crt + 1

	if crt < alter:
		l[n - 1] = alter

	for i in range(n - 2, -1, - 1):
		crt = l[i]
		alter = n - crt + 1

		if (crt < alter or crt > l[i + 1])and alter <= l[i + 1]:
			l[i] = alter
	
	for i in range(n - 1):
		if l[i] > l[i + 1]:
			p("NO")
			return
	p("YES")

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()