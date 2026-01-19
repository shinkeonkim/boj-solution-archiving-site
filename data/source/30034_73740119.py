import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  N = ii()
  a = input().split()
  
  M = ii()
  b = input().split()
  
  K = ii()
  c = input().split()
  
  a = [i for i in a if i not in c]
  b = [i for i in b if i not in c]
  
  input()
  s = input()
  
  crt = ""
  ans = []

  for i in s:
    if i in a or i in b or i == " ":
      if crt != "":
        ans.append(crt)
      crt = ""
    else:
      crt += i
  if crt != "":
    ans.append(crt)
  
  p(*ans, sep="\n")
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
