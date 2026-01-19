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
    l = mii()

    count = {}

    for i in l:
        count[i] = count.get(i, 0) + 1
    
    cnt = sorted([*count.values()])

    if 3 in cnt and 2 in cnt:
        return "full house"
    
    if 4 in cnt:
        if 2 in cnt:
            return "tiki pair"
        return "tiki"
    
    if cnt.count(3) == 2:
        return "two triples"
    
    if 3 in cnt:
        return "one triple"
    
    if cnt.count(2) == 3:
        return "three pairs"
    
    if cnt.count(2) == 2:
        return "two pairs"
    
    if cnt.count(2) == 1:
        return "one pair"
    
    return "single"


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()
        p(ret)