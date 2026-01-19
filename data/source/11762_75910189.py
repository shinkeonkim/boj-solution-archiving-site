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
	*l, A, B = mii()

	l.sort()

	s = sum(l)

	chk = False
	for i in range(6):
		for j in range(i + 1, 6):
			for k in range(j + 1, 6):
				if l[i] + l[j] + l[k] == A:
					z = [i, j, k]
					chk = True
					break
			if chk:
				break
		if chk:
			break

	z2 = [*({0, 1, 2, 3, 4, 5} - set(z))]

	z = z[::-1]
	z2 = z2[::-1]

	for i in z + z2:
		p(l[i], end = " ")



if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()