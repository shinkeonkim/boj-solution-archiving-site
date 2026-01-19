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
    n, m, k = mii()
    l = [inp() for _ in range(n)]

    leng = []
    for i in range(n):
        cnt = 0
        
        for j in range(m):
            if l[i][j] == '#':
                if cnt > 0:
                    leng.append(cnt)
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            leng.append(cnt)
    for j in range(m):
        cnt = 0
        for i in range(n):
            if l[i][j] == '#':
                if cnt > 0:
                    leng.append(cnt)
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            leng.append(cnt)
    
    ans = 0
    for i in leng:
        ans += max(0, i - k + 1)

    p(ans)

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
