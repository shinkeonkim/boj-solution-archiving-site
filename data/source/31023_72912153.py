import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  ret = ""
  for i in s:
    if 'a' <= i <= 'z':
      ret += i
    else:
      ret += " "      
  return ret


def solve():
  n = ii()
  words = [inp() for _ in range(n)]
  
  k = ii()
  sentences = [f(inp().lower()) for _ in range(k)]
  
  total = 0
  cnt = 0
  
  for sentence in sentences:
    for word in sentence.split():
      if word in words:
        cnt += 1
      total += 1
  
  p("It's a hit!" if cnt * 4 >= 3 * total else "Delete immediately!")
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
