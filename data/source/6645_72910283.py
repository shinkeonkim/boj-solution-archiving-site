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
  while 1:
    s = input()
    
    if s == "0 END":
      break
    
    n, name = s.split()
    n = int(n)
    
    l = [input().split() for _ in range(n)]
    
    p(name)
    
    for i in range(n):
      name, cat, price = l[i]
      price = float(price)
      ans = []
      for j in range(n):
        o_name, o_cat, o_price = l[j]

        if cat == o_cat or i == j:
          continue
        o_price = float(o_price)

        if cat == "buy" and price >= o_price:
          ans.append(o_name)
        
        if cat == "sell" and price <= o_price:
          ans.append(o_name)

      p(f"{name}: ", end="")

      if len(ans) == 0:
        p("NO-ONE")
      else:
        p(*ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
