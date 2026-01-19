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
    n = ii() # total number of water main breaks
    s, f = mii() # start time, finish time

    l = [mii() for _ in range(n)]
    ans = 0

    for s_i, f_i, r_i in l:
        a = max(s, s_i)
        b = min(f, f_i)

        if a > b:
            continue
        
        diff = b - a + 1

        ans += diff * r_i
    p(ans)


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        p(f"Data Set {t}:")
        ret = solve()
        p()
