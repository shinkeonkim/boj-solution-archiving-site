import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(s):
  flag = 0
  
  for i in s:
    if 'A' <= i <= 'Z':
      flag |= 1
    if 'a' <= i <= 'z':
      flag |= 2
    if '0' <= i <= '9':
      flag |= 4
  return flag == 7


def solve():
  s = input()
  
  for l in range(6, len(s) + 1):
    for start in range(0, len(s)):
      if start + l > len(s):
        break
      
      crt = s[start:start+l]
      
      if f(crt):
        return l
  return 0
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
   