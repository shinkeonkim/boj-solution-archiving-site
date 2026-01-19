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

def solve():
    d = {"C": 12010, "H": 1008, "O": 16000, "N": 14010}

    s = inp()

    l = []
    cnt = 0
    crt = ""
    for i in s:
        if i in "CHON":
            # 기존 값 처리
            if crt != "":
                if cnt == 0:
                    cnt = 1
                l.append([crt, cnt])

            crt = i
            cnt = 0
        else:
            num = int(i)
            cnt *= 10
            cnt += num  

    if cnt == 0:
        cnt = 1
    l.append([crt, cnt])

    ans = 0
    for category, cnt in l:
        ans += d[category] * cnt

    p(f"{ans // 1000}.{ans % 1000:03d}")

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()