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
	cnt = mii()
	
	ticket = mii()

	ans = [0] * 3


	for i in range(3):
		ans[i] = min(cnt[i], ticket[i])
		cnt[i] -= ans[i]
		ticket[i] -= ans[i]

	for _ in range(1000):
		A = ticket[0] // 3
		B = ticket[1] // 3
		C = ticket[2] // 3

		ticket[0] = ticket[0] % 3 + C
		ticket[1] = ticket[1] % 3 + A
		ticket[2] = ticket[2] % 3 + B

		for i in range(3):
			z = min(cnt[i], ticket[i])
			ans[i] += z
			cnt[i] -= z
			ticket[i] -= z

	p(sum(ans))



if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
