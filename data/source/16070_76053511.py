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
    n = ii()
    hero = mii()
    villain = mii()

    for weight in range(0, 2000):
        chk = True

        for idx in range(n):
            if villain[idx] > hero[idx] + weight:
                chk = False
                break
            if villain[idx] < hero[idx] + weight:
                break
            
        
        if chk:
            p(weight)
            break



if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
