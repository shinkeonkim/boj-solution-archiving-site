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

def f(ar, sz):
	l = [{}, {"@": 0}, {}]

	for i in range(3):
		for j in range(sz):
			row = sz * i + j

			for ch in ar[row]:
				l[i][ch] = l[i].get(ch, 0) + 1
	

	l = [[*i.items()] for i in l]

	ans = 1e10

	for i in range(len(l[0])):
		for j in range(len(l[1])):
			for k in range(len(l[2])):
				A = l[0][i]
				B = l[1][j]
				C = l[2][k]

				if A[0] == B[0] or C[0] == B[0]:
					continue
				
				ans = min(ans, 54 - A[1] - B[1] - C[1])
	return ans

def solve():
	ar = [inp() for _ in range(6)]
	ans = f(ar, 2)

	ar2 = []

	for i in range(9):
		z = ""
		for j in range(6):
			z += ar[j][i]
		ar2.append(z)

	ans = min(ans, f(ar2, 3))

	p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()