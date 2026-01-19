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

	left = [True for i in range(1, n + 1)]
	
	crt = 0

	for stage in range(n - 1):
		k = (stage + 1) ** 3 - 1

		k %= n - stage

		cnt = 0
		while 1:
			if cnt == k and left[crt % n]:
				break
			if left[crt % n]:
				cnt += 1
			crt += 1
		
		left[crt % n] = False
		crt += 1

	p(left.index(True) + 1)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
