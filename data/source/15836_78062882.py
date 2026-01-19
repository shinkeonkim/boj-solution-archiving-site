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
    tc = 1

    while 1:
        a, b, c, d = mii()

        if a == b == c == d == 0:
            break

        p(f"Case #{tc}:")
        tc += 1

        X = [[*map(int, inp().split())] for _ in range(a)]

        Y = [[*map(int, inp().split())] for _ in range(c)]

        if b != c:
            p("undefined")
            continue

        for i in range(a):
            p(end="| ")
            for j in range(d):
                ret = 0
                for k in range(b):
                    ret += X[i][k] * Y[k][j]

                p(ret, end=" ")
            p("|")

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()