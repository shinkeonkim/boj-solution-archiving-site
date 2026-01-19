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
	n, q = mii() # q : 집까지 가는 시간

	ans = [0, 1e40]
	for i in range(1, n + 1):
		price, k, c = mii() # p: 가격, k: 추가 비용 간격, C : 추가 비용 초기값

		t = q // k + (-1 if q % k == 0 else 0)

		price = price + (t * (t + 1) // 2) * c

		if ans[1] > price:
			ans = [i, price]
	p(*ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()