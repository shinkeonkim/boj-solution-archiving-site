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

def sign(a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    return 0

def solve():
    s = [*map(int, list(inp()))]

    diff = []

    for i in range(len(s) - 1):
        diff.append(s[i + 1] - s[i])

    chk = True

    for i in range(1, len(diff)):
        prev = diff[i - 1]
        crt = diff[i]

        if sign(prev) == sign(crt):
            if prev != crt:
                chk = False
        
        if sign(prev) == 0 or sign(crt) == 0:
            chk = False
        
    
    if sign(diff[0]) <= 0 or sign(diff[-1]) >= 0:
        chk = False
    

    p("ALPSOO" if chk else "NON ALPSOO")


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()