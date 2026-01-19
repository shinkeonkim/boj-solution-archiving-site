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

def num(s):
	if s == " ":
		return 26
	
	return ord(s) - 97


def solve():
	z = [
		"2", "22", "222",
		"3", "33", "333",
		"4", "44", "444",
		"5", "55", "555",
		"6", "66", "666",
		"7", "77", "777", "7777",
		"8", "88", "888",
		"9", "99", "999", "9999",
		"0"
	]

	s = input()
	ans = ""

	ans += z[num(s[0])]

	for i in range(1, len(s)):
		crt = z[num(s[i])]

		if crt[0] == ans[-1]:
			ans += " "
		ans += crt
	
	return ans
	



if __name__ == "__main__":
	tc = ii()
	for t in range(1, tc+1):
		ret = solve()
		p(f"Case #{t}: {ret}")
