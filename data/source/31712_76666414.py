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

def solve():
    l = [mii() for _ in range(3)]

    H = ii()

    for _, d in l:
        H -= d

    if H <= 0:
        p(0)
        return

    start = 1
    end = 10000000000

    ans = end

    while start <= end:
        mid = (start + end) // 2

        total_dmg = 0
        for c, d in l:
            total_dmg += (mid // c) * d

        if total_dmg >= H:
            ans = min(ans, mid)
            end = mid - 1
        else:
            start = mid + 1

    p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()