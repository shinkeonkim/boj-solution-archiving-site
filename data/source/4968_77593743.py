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
    while 1:
        n, m = mii()

        if n == m == 0:
            break

        a = [ii() for _ in range(n)]
        b = [ii() for _ in range(m)]

        mn = 1e30
        ans = []

        for i in a:
            for j in b:
                A = sum(a) - i + j
                B = sum(b) - j + i

                if A == B and mn > i + j:
                    mn = i + j
                    ans = [i, j]

        if mn == 1e30:
            p(-1)
        else:
            p(*ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()