import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  happy = 0
  sad = 0
  for i in s:
    if i in "APHYaphy":
      happy += 1
    if i in "ASDasd":
      sad += 1
  
  if happy == sad == 0:
    p("50.00")
  else:
    k = happy * 100 / (happy + sad)
    
    a = (happy * 100000 // (happy + sad)) // 1000
    b = happy * 100000 // (happy + sad) % 1000
    
    if b % 10 >= 5:
      b = (b // 10) + 1
    else:
      b = (b // 10)
    
    while b > 99:
      a += 1
      b = b % 100
    
    p(f"{a}.{b:02d}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

