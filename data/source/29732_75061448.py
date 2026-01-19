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
	s = inp()

	# m: 치료제 개수, k: 전염 범위

	chk = [(1 if i == 'R' else 0) for i in s]

	patients = []

	for i in range(n):
		if chk[i]:
			patients.append(i)
	
	
	for patient in patients:
		for r in range(max(0, patient - k), min(n - 1, patient + k) + 1):
			if chk[r] == 0:
				chk[r] = 2
	
	z = n - chk.count(0)

	p("No" if z > m else "Yes")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()