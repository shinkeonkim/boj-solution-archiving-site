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
    d = {9:34, 40:64, 67:86, 54:19, 90:48, 99:77}

    crt = 1
    while 1:
        n = ii()

        if n == 0:
            p("You Quit!")
            break

        crt += n

        if crt > 100:
            crt -= n

        if crt in d:
            crt = d[crt]
        
        p(f"You are now on square {crt}")

        if crt == 100:
            p("You Win!")
            break

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
