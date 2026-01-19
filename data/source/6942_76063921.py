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


def f(num):
    s = str(num)

    for i in "23457":
        if i in s:
            return False
    
    reverse = ""

    for i in s[::-1]:
        if i == "6":
            reverse += "9"
        elif i == "9":
            reverse += "6"
        else:
            reverse += i
    
    return reverse == s


def solve():
    m = ii()
    n = ii()
    ans = 0

    for i in range(m, n + 1):
        if f(i):
            ans += 1
    
    p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
