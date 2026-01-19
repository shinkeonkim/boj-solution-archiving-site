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

def solve():
    n, M = input().split()
    n = int(n)
    M = float(M)

    l = [mfi() for _ in range(n)]

    g = 9.81
    
    current_m = M
    ans = 0

    for m, t, F in l:
        current_m += m

    v = 0
    for m, t, F in l:
        a = F / current_m - g

        ans += v * t + 1 / 2 * a * t * t
        v += a * t

        current_m -= m 

    p(f"{ans:.2f}")


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        p(f"Data Set {t}:")
        ret = solve()