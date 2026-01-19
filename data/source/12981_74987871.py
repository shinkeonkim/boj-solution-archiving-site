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
	R, G, B = mii()

	ans = 0
	z = min(R, G, B)

	ans += z

	R -= z
	G -= z
	B -= z

	ans += R // 3
	R %= 3
	ans += G // 3
	G %= 3
	ans += B // 3
	B %= 3

	l = [R, G, B]

	if l.count(1) == 2:
		ans += 1
	else:
		ans += (R + 1) // 2 + (G + 1) // 2 + (B + 1) // 2
	
	p(ans)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
