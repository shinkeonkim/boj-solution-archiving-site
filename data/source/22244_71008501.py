import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  d = int(s[:2])
  m = int(s[2:4])
  y = int(s[4:7])
  y2 = 2000 + y if y <= 599 else 1000 + y
  author = int(s[7])
  chk = int(s[8])
  
  
  if m < 1 or m > 12:
    return 0
  
  if author not in [1, 6, 9]:
    return 0
  
  sm = 0
  for i in s[:-1]:
    sm += int(i) ** 2
  
  if sm % 7 != chk:
    return 0
  
  leap_year = y2 % 4 == 0 and (y2 % 100 != 0 or y2 % 400 == 0)
  month_days = [
    31, (29 if leap_year else 28), 31, 30,
    31, 30, 31, 31, 
    30, 31, 30, 31
  ]
  
  if d < 1 or d > month_days[m - 1]:
    return 0
  
  return 1
                               
  
  
if __name__ == "__main__":
  tc = 3
  
  for t in range(1, tc+1):
    d = solve()
    p(d)
