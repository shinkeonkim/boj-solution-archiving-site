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
    d = {"A#":"Bb", "Bb":"A#", "C#":"Db", "Db":"C#", "D#":"Eb", "Eb": "D#", "F#": "Gb", "Gb": "F#", "G#": "Ab", "Ab": "G#"}
    tc = 1
    while 1:
        try:
            a, b = input().split()
        except:
            break

        p(f"Case {tc}: ", end="")
        if a in d:
            p(d[a], b)
        else:
            p("UNIQUE")


        tc += 1

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
