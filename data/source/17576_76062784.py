import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)
from functools import reduce

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
    s = input()    
    n = ii()

    left, right = 0, len(s) + 1
    for _ in range(n):
        start, length = mii()

        left += start
        right = left + length
    
    p(s[left:right])


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
