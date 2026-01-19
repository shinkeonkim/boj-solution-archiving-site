import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
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
  
  # A, H, O, W
  # WW, HH 불가
  # HA 또는 HW 불가
  # 첫 O 뒤에 A 불가
  
  # "WHOHO" +"WHOHA"
  
  z = len(s) - 6
  
  p("AWHOHO" + "WHOHO" * (z // 5 + 1))
    
  
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
