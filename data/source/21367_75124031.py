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
	n, q = mii()

	cap = mii()
	waiting = mii()

	total = sum(cap)

	waiting_idx = [[idx, waiting[idx], -1] for idx in range(q)]

	waiting_idx.sort(key = lambda t : t[1])

	capacity = [cap[0]]

	for i in range(1, n):
		capacity.append(capacity[-1] + cap[i])
	
	i = 0
	j = 0
	
	while i < n and j < q:
		if waiting_idx[j][1] + 1 <= capacity[i]:
			waiting_idx[j][2] = i + 1
			j += 1
		else:
			i += 1

	waiting_idx.sort(key = lambda t : t[0])

	for _, _, i in waiting_idx:
		p(i)


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
