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

def diff(a, b):
    ret = 0
    for i in range(5):
        for j in range(5):
            if a[i][j] != b[i][j]:
                ret += 1

    return ret


def f(data, query):
    dif = []
    ret = []

    for datum in data:
        dif.append(diff(datum, query))
    
    mn = min(dif)

    for i in range(len(data)):
        if dif[i] == mn:
            ret.append(i + 1)
    
    return ret


def solve():
    n, k = mii()

    data = []

    for _ in range(n):
        l = [inp() for _ in range(5)]
        data.append(l)
    
    for tc in range(1, k + 1):
        query = [inp() for _ in range(5)]

        ret = f(data, query)

        p(f"Data Set {tc}:")
        p(*ret)
        p()


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
