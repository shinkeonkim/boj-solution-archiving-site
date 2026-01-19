import sys
from math import sqrt, pi, sin, cos, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
prt = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def f(s, w):
  ret = ""

  for i in s:
    if 'A' <= i <= 'Z':
      ret += chr((ord(i) - 65 + w) % 26 + 65)
    else:
      ret += i
  return ret

def solve():
  cipher = input()

  for i in range(26):
    crt = f(cipher, i)
    if "CHIPMUNKS" in crt and "LIVE" in crt:
      prt(crt)
      break


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

