import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  N = ii()
  
  channels = [inp() for _ in range(N)]
  
  crt = 0
  for i in range(N):
    if channels[i] == "KBS1":
      break
    
    crt += 1
    p("1",end="")
  
  channels = [channels[crt]] + channels[:crt] + channels[crt + 1 :]
  
  for i in range(crt):
    p("4",end="")
  
  crt = 0
  for i in range(N):
    if channels[i] == "KBS2":
      break
    
    crt += 1
    
    p("1",end="")
  
  for i in range(crt - 1):
    p("4",end="")
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()