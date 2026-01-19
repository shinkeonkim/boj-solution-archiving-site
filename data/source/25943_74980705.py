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
  

def solve():
	n = ii()
	l = mii()

	a = b = 0

	for i in l:
		if a <= b:
			a += i
		else:
			b += i

	diff = abs(a - b)

	z = [100, 50, 20, 10, 5, 2, 1]

	cnt = 0 

	for i in z:
		cnt += diff // i
		diff %= i

	p(cnt)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
