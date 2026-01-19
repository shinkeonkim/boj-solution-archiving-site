import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
    sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def to_num(s):
	a, micro = s.split(",")
	micro = int(micro)
	h, m, s = map(int, a.split(":"))

	return micro + s * 1000 + m * 60000 + h * 3600000


def to_str(num):
	micro = num % 1000
	num //= 1000
	s = num % 60
	num //= 60
	m = num % 60
	num //= 60
	
	return f"{num:02d}:{m:02d}:{s:02d},{micro:03d}"


def f(el, diff, is_end = False):
	n, timeline, text = el
	
	start, end = timeline.split(" --> ")
	start = to_num(start) + diff
	end = to_num(end) + diff

	p(n)
	p(f"{to_str(start)} --> {to_str(end)}")
	p(*text, sep="\n")
	if is_end:
		p("#")
	else:
		p()


def solve():
	exit = False

	ar = []

	while 1:
		n = ii()
		timeline = inp()

		text = []

		while 1:
			k = inp()

			if k == "#":
				exit = True
				break

			if k == "":
				break
			
			text.append(k)
		

		ar.append([n, timeline, text])

		if exit:
			break

	diff = ii()
	
	for idx in range(len(ar)):
		f(ar[idx], diff, idx == len(ar) - 1)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()