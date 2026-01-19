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
    odd = []
    even = []

    odd_idx = []
    even_idx = []

    n = ii()
    l = mii()

    for idx in range(n):
        i = l[idx]

        if abs(i) % 2:
            odd.append(i)
            odd_idx.append(idx)
        else:
            even.append(i)
            even_idx.append(idx)
    
    odd.sort()
    even.sort(reverse=True)

    ans = [0] * n


    for i in range(len(odd)):
        ans[odd_idx[i]] = odd[i]
    
    for i in range(len(even)):
        ans[even_idx[i]] = even[i]

    p(*ans)

if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        p(f"Case #{t}: ", end="")
        ret = solve()
