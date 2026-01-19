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


mapping = {
    'A': 0,
    'A#': 1,
    'B': 2,
    'C': 3,
    'C#': 4,
    'D': 5,
    'D#': 6,
    'E': 7,
    'F': 8,
    'F#': 9,
    'G': 10,
    'G#': 11
}

rev_mapping = {}

for k, v in mapping.items():
    rev_mapping[v] = k

def to_num(c):
    if 'b' in c:
        return (mapping[c[0]] - 1 + 12) % 12
    
    if c in mapping:
        return mapping[c]

    if '#' in c:
        return (mapping[c[0]] + 1 + 12) % 12

    return mapping[c]


def solve():

    while 1:
        s = input()
        if s == "***":
            break

        n = ii()
        
        l = s.split()

        for code in l:
            num = to_num(code)

            p(rev_mapping[(num + n + 12) % 12], end = " ")
        p()





if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
