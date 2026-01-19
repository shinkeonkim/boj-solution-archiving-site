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

def f(l):
    ret = []
    
    l2 = [l[i] for i in range(1, 10, 2)]

    for i in range(5):
        for j in range(i + 1, 5):
            ret.append(abs(l2[i] - l2[j]))

    return len(set(ret)) == len(ret)


def g(l):
    s = set()

    for i in range(0, 10, 2):
        s.add(l[i])

    return len(s) == 5


def solve():
    l = mii()
    
    is_spread = f(l)
    is_rainbow = g(l)


    p("Have a spread.          " if is_spread else "Do not have a spread.   ", end="")
    p("Have a rainbow." if is_rainbow else "Do not have a rainbow.")

if __name__ == "__main__":
    tc = ii()

    for t in range(1, tc+1):
        ret = solve()