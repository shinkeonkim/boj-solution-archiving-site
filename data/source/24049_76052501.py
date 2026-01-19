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
    n, m = mii()
    l = [[-1] * (m + 1) for _ in range(n + 1)]

    a = mii()
    b = mii()

    for i in range(1, n + 1):
        l[i][0] = a[i - 1]

    for i in range(1, m + 1):
        l[0][i] = b[i - 1]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            l[i][j] = 0 if l[i - 1][j] == l[i][j - 1] else 1
    
    p(l[n][m])
    


if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()