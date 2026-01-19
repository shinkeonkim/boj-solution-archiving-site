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

z = [
	"","",
	"ABC",
	"DEF",
	"GHI",
	"JKL",
	"MNO",
	"PQRS",
	"TUV",
	"WXYZ"
]

def f(s):
	ret = ""
	for i in range(len(s)):
		crt = s[i]

		lower = False
		if crt.lower() == crt:
			lower = True
			crt = crt.upper()

		target = ""
		for j in range(2, 10):
			if crt in z[j]:
				target = z[j]
		
		idx = target.index(crt)
		idx = (idx - (i + 1) + len(target)) % len(target)


		ret += target[idx].lower() if lower else target[idx]

	return ret



def solve():
	while 1:
		s = inp()

		if s == "#":
			break
		p(f(s))


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()