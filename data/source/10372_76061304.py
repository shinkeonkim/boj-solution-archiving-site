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

def f(a):
    cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    return cnt[a // 10] + cnt[a % 10]


def solve():

    n = ii()

    for h in range(24):
        for m in range(60):
            if n == f(h) + f(m):
                return f"{h:02d}:{m:02d}"

    return "Impossible"

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
        p(ret)
