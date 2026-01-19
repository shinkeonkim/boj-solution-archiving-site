import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
    sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def f(s, target):
    n = len(s)
    cnt = 0
    chk = False
    for i in range(n):
        if s[i] == target:
            if chk:
                cnt += 1
        else:
            chk = True

    return cnt

def solve():
    n = ii()
    s = inp()

    ans = 1e20
    # 1. B를 왼쪽으로 모는 경우

    ans = min(ans, f(s, "B"))
    ans = min(ans, f(s[::-1], "B"))
    ans = min(ans, f(s, "R"))
    ans = min(ans, f(s[::-1], "R"))

    p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()