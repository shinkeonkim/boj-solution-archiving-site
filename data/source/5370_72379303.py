import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    try:
      n = ii()
    except:
      break
    
    s = bin(n)[2:]
    
    a = s.count("0")
    b = s.count("1")
    
    if a > b:
      print("left")
    elif a < b:
      print("right")
    else:
      print("straight")
    

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

