import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(row, col):
  col += 1   
  if row == 21 and col == 5:
    row = 1
    col = 3

  if col == 6:
    row += 1
    col = 0

  if row == 21 and col == 0:
    col = 3
  
  return (row, col)


def solve():
  n = ii()
  s = input()
  
  if n == 118:
    p("full")
    return
  
  r = int(s[:-1])
  c = ord(s[-1]) - 65
  
  row = 1
  col = 3

  idx = 0

  if r == row and col == c:
    col += 1
  
  while idx < n:
    idx += 1
    
    if row == r and col == c:
      idx -= 1
    
    row, col = f(row, col)
  
  if row == r and col == c:
    row, col = f(row, col)
  
  p(f"{row}{chr(col+65)}")
    
  
tc = 1

for t in range(1, tc+1):
  ret = solve()
  
