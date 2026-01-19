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
    n, q = mii()
    l = mii()

    queries = [mii() for _ in range(q)]
    d = [0]
    
    for i in l:
        d.append(d[-1] + i)

    sm = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sm.append(d[j] - d[i])

    sm.sort()

    d = [0]

    for i in sm:
        d.append(d[-1] + i)
    
    for a, b in queries:
        p(d[b] - d[a - 1])
    


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        p(f"Case #{t}:")
        ret = solve()
