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
	n, m, k = mii()

	if m == 1 and k == 1 and n > 1:
		p(-1)
		return

	# n명, m개의 우산, k명 최대

	# 창의 (m개의 우산) -> 융합

	crt = m
	ans = 0

	while n > 0:
		ans += 1
		if crt == 0:
			# 우산 가져오기
			n += 1
			crt = m
			ans += 1

		need_umb = n // k + int(n % k > 0)

		use = min(crt, need_umb)

		n -= use * k
		crt -= use
	
	p(ans)


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()