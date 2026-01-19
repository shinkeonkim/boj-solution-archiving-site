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
#    2
#  3 1 4 6 
#    5


def solve():
    while 1:
        n = ii()

        if n == 0:
            break
        crt = [2, 3, 1, 4, 6, 5]

        for _ in range(n):
            query = inp()

            if query == "north":
                crt[0], crt[2], crt[5], crt[4] = crt[2], crt[5], crt[4], crt[0]
            if query == "south":
                crt[2], crt[5], crt[4], crt[0] = crt[0], crt[2], crt[5], crt[4]
            if query == "east":
                crt[2], crt[3], crt[4], crt[1] = crt[1], crt[2], crt[3], crt[4]
            if query == "west":
                crt[1], crt[2], crt[3], crt[4] = crt[2], crt[3], crt[4], crt[1]
        p(crt[2])




if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
