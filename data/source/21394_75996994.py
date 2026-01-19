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
    l = [0] + mii()

    prev = ""

    d = []

    for i in range(1, 10):
        if i == 6:
            d.extend([9] * l[i])
        else:
            d.extend([i] * l[i])

    d.sort(reverse = True)

    left = 0
    right = len(d) - 1

    ans = [0] * len(d)

    idx = 0
    while left <= right:
        if left == right:
            ans[left] = d[idx]
            break
        else:
            ans[left] = d[idx]
            idx += 1
            ans[right] = d[idx]
            idx += 1
        
        left += 1
        right -= 1 

    p(*ans)

if __name__ == "__main__":
    tc = ii()

    for t in range(1, tc+1):
        ret = solve()