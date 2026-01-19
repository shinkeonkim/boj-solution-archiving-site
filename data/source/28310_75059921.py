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
	n, m = mii() # N: 고양이, M: 과자
	l = [mii() for _ in range(m)]

	total = 1
	for i in l:
		total = lcm(total, i[0])

	cnt = [0] * n

	for i in l:
		mul = total // i[0]

		for j in range(n):
			cnt[j] += i[j + 1] * mul
	
	A = max(cnt) - min(cnt)
	B = total

	A, B = A // gcd(A, B), B // gcd(A, B)

	if A % B == 0:
		p(A // B)
	else:
		p(f"{A}/{B}")


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()