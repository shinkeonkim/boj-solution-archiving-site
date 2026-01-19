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
	participants = [inp() for _ in range(n)]

	cnt1 = [0] * 3 # 백신을 맞았을 때 걸린 사람.?
	cnt2 = [0] * 3 # 백신을 안 맞았을 때, 걸린 사람
	y_cnt = 0

	for par in participants:
		flag = par[0]

		if flag == "Y":
			y_cnt += 1

		for i in range(3):
			if par[i + 1] == "Y" and flag == "Y":
				cnt1[i] += 1
			if par[i + 1] == "Y" and flag == "N":
				cnt2[i] += 1
	x = n - y_cnt
	for i in range(3):
		if cnt1[i] / y_cnt >= cnt2[i] / x:
			p("Not Effective")
		else:
			p(100 * x * (cnt2[i] / x - cnt1[i] / y_cnt) / cnt2[i])
	

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()