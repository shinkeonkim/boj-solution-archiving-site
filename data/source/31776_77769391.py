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

def f(l):
    if l[0] == - 1:
        return 0

    if l[1] == - 1:
        if l[2] >= 0:
            return 0
        return 1

    if l[2] == -1:
        return int(l[0] <= l[1])

    return int(l[0] <= l[1] <= l[2])

def solve():
    n = ii()
    l = [mii() for _ in range(n)]

    ans = 0

    p(sum([f(i) for i in l]))            

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()