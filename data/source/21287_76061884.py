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
    R = G = B = False

    n = ii()
    s = inp()

    ans = ""
    for i in s:
        if i == 'R':
            R = True
        if i == 'G':
            G = True
        if i == 'B':
            B = True
        
        if R and G and B:
            ans += i
            R = G = B = False

    if len(ans) < n:
        ans += "R" * (n - len(ans))
    p(ans[:n])

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
