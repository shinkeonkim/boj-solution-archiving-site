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
	n, k = mii() # n: 플레이어가 가진 카드 수, k: 무작위 선택 카드
	a = mii() # n개, Grisha
	b = mii() # n개, Dima

	a.sort()
	b.sort()

	a = sum(a[:k])
	b = sum(b[-k:])

	if a > b:
		p("YES")
	else:
		p("NO")



if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		ret = solve()
