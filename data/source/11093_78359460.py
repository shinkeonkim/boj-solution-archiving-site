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
    s = inp()

    n = len(s)

    k = 0

    while k * k < n:
        k += 1

    l = []

    for i in range(0, k * k, k):
        l.append(s[i:i+k])

    ans = ""
    for j in range(k):
        for i in range(k - 1, -1, -1):
            ans += "".join(l[i][j:j+1])
    p(ans)

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()