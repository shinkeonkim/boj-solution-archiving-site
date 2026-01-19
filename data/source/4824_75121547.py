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

def f(l):
	return l[2] + (l[0] + l[1]) * 2 <= 2100

def solve():
	# letter: 길이 125 ~ 290, 높이: 90 ~ 155, 두께: 0.25 ~ 7
	# packet: 길이 380 이하, 높이 300 이하, 두께 50 이하
	# 


	while 1:
		s = inp()
		
		if s == "0 0 0":
			break

		l = sorted([*map(float, s.split())])

		if 0.25 <= l[0] <= 7 and 90 <=l[1] <= 155 and 125 <= l[2] <= 290:
			p("letter")
		elif 0.25 <= l[0] <= 50 and 90 <= l[1] <= 300 and 125 <= l[2] <= 380 and (7 <= l[0] or 155 <= l[1] or 290 <= l[2]):
			p("packet")
		elif 0.25 <= l[0] and 90 <= l[1] and 125 <= l[2] and (50 <= l[0] or 300 <= l[1] or 380 <= l[2]) and f(l):
			p("parcel")
		else:
			p("not mailable")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()