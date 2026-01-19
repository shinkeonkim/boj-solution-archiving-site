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

def rotate(l):
	ret = []
	n = len(l)

	for i in range(n):
		l2 = []
		for j in range(n - 1, -1, -1):
			l2.append(l[j][i])
		ret.append(l2)
	
	return ret


def solve():
	n = ii()

	l = [list(inp()) for _ in range(n)]

	s = inp()

	chk = [l[i][::] for i in range(n)]
	cnt = 0

	for i in range(4):
		for i in range(n):
			for j in range(n):
				if l[i][j] == '.':
					if cnt >= len(s):
						return "invalid grille"
					chk[i][j] = s[cnt]
					cnt += 1

	
		l = rotate(l)
	
	ans = ""

	for i in chk:
		for j in i:
			if j == "." or j == "X":
				return "invalid grille"
			ans += j
	return ans



if __name__ == "__main__":
	tc = 1
	for t in range(1, tc+1):
		ret = solve()
		p(ret)
