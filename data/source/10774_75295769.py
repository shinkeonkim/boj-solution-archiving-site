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
	J = ii() # 저지의 수
	A = ii() # 선수의 수

	ans = 0
	l = [""] + [inp() for _ in range(J)]

	d = {"S": 0, "M": 1, "L": 2}

	for i in range(A):
		size, num = inp().split()
		num = int(num)

		if l[num] == "":
			continue
		
		if d[l[num]] >= d[size]:
			ans += 1
			l[num] = ""
	p(ans)



if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
