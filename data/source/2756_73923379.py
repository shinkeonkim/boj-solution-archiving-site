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

def f(A):
  for a, b in [[9, 100], [36, 80], [81, 60], [144, 40], [225, 20]]:
    if A <= a:
      return b
  
  return 0

def solve():
  l = mfi() # 12개
  
  A = 0
  B = 0
  for i in range(6):
    x = l[2 * i]
    y = l[2 * i + 1]
    
    score = f(x * x + y * y)
    
    if i < 3:
      A += score
    else:
      B += score
  
  if A == B:
    p(f"SCORE: {A} to {B}, TIE.")
  elif A > B:
    p(f"SCORE: {A} to {B}, PLAYER 1 WINS.")
  else:
    p(f"SCORE: {A} to {B}, PLAYER 2 WINS.")
    
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
