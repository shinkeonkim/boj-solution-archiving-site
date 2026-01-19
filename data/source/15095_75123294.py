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
	l = [inp() for _ in range(5)]

	cnt = 0

	for i in l:
		cnt += i.count("k")
	
	if cnt != 9:
		return "invalid"
	
	dx = [-2, -1, 1, 2, 2, 1, -1, -2]
	dy = [1, 2, 2, 1, -1, -2, -2, -1]

	for i in range(5):
		for j in range(5):
			if l[i][j] == 'k':
				for d in range(8):
					ny = i + dy[d]
					nx = j + dx[d]

					if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
						continue
					
					if l[ny][nx] == 'k':
						return "invalid"

	return "valid"


if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
		p(ret)
