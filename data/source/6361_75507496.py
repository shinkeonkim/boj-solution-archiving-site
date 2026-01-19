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

def to_num(c):
	if 'a' <= c <= 'z':
		return ord(c) - 61
	
	if 'A' <= c <= 'Z':
		return ord(c) - 55
	
	return int(c)
	
def to_char(num):
	if 36 <= num:
		return chr(num + 61)

	if 10 <= num:
		return chr(num + 55)
	
	return str(num)

def solve():
	a, b, s = input().split()
	a = int(a)
	b = int(b)

	crt = 0
	for i in s:
		crt *= a
		crt += to_num(i)
	
	ans = ""
	while crt > 0:
		ans += to_char(crt % b)
		crt //= b
	if ans == "":
		ans = "0"

	p(a, s)
	p(b, ans[::-1])
	p()

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()