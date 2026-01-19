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


months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

def solve():
  m, d, y = input().split()
  d = int(d[:-1])
  y = int(y)
  
  if d < 1 or d > 31:
    return "Invalid"
  
  for i in range(12):
    month = months[i]
  
    if month != m:
      continue
    
    return f"{i+1:02d}/{d:02d}/{(y % 100):02d}"
    
  
  return "Invalid"
    

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(ret)