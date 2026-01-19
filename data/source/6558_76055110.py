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


def to_num(st):
    h, m, s = map(int, st.split(":"))

    return h * 3600 + m * 60 + s


def solve():
    n, distance = input().split()
    n = int(n)
    distance = float(distance)

    while 1:
        try:
            s = input()
        except:
            break
        
        s = s.strip()

        a, *l = s.split()
        a = int(a)
        
        if "-:--:--" in l:
            p(f"{a:>3}: -")
            continue

        sm = 0
        for i in l:
            sm += to_num(i)

        
        z = round(sm / distance)

        p(f"{a:>3}: {z // 60}:{z % 60:02d} min/km")



if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
