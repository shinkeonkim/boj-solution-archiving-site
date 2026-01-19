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

def f(l, s):
    fd = s * 3
    for i in l:
        if fd in i:
            return True
        
    
    for i in range(5):
        k = ""
        for j in range(5):
            k += l[j][i]
        
        if fd in k:
            return True
    
    for i in range(5):
        for j in range(5):
            tmp = ""
            tmp2 = ""
            for k in range(5):
                if i + k < 5 and j + k < 5:
                    tmp += l[i + k][j + k]
                else:
                    break

            for k in range(5):
                if i - k >= 0 and j + k < 5:
                    tmp2 += l[i - k][j + k]
                else:
                    break
            if fd in tmp or fd in tmp2:
                return True
    return False


def solve():
    l = [inp() for _ in range(5)]

    A = f(l, "A")
    B = f(l, "B")


    if A == B:
        p("draw")
    elif A:
        p("A wins")
    else:
        p("B wins")


if __name__ == "__main__":
    tc = ii()
    for t in range(1, tc+1):
        ret = solve()