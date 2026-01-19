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
    n, c = input().split()
    s = input()
    n = int(n)

    cnt = {}

    for i in s:
        cnt[i] = cnt.get(i, 0) + 1

    mx = max(cnt.values())

    target = ""
    for i in s:
        if cnt[i] == mx:
            target = i
    
    diff = ord(c) - ord(target) 

    for i in s:
        p(end=chr((ord(i) - 65 + diff + 26) % 26 + 65))

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
