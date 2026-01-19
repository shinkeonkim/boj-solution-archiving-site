import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = False
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


def f(l, k):
    n = len(l)
    l.sort(reverse=True)

    ans = 0
    mx = 0

    for i in range(n):
        mx = max(mx, l[i])

        if (i + 1) % k == 0:
            ans += mx * 2
            mx = 0

    ans += mx * 2
    return ans

def solve():
    n, k = mii()

    ar = [ii() for _ in range(n)]

    minus = [-i for i in ar if i < 0]
    plus = [i for i in ar if i > 0]

    ans = f(minus, k) + f(plus, k)
    p(ans)


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()