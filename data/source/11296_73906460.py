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

def solve():
  price, dot, coupon, flag = input().split()
  
  d = {"R": 45, "G": 30, "B": 20, "Y": 15, "O": 10, "W": 5}

  percent = d[dot]
  
    
  a, b = map(int, price.split("."))
  
  price = a * 100 + b

  if flag == 'P':
    k = price * (100 - percent) / 10000
    
    if coupon == "C":
      k = k * 95 / 100
    print(f"${k:.2f}")
  else:
    if coupon == "X":
      A = price * (100 - percent)

      Z = A // 10000
      B = A % 10000 // 100
      
      if B % 10 > 5:
        B //= 10
        B += 1
      else:
        B //= 10
      B *= 10
      
      Z += B // 100
      B %= 100
  
      p(f"${Z}.{B:02d}")    
    else:
      A = price * (100 - percent) * 95

      Z = A // 1000000
      B = A % 1000000 // 10000
      
      if B % 10 > 5:
        B //= 10
        B += 1
      else:
        B //= 10
      B *= 10
      
      Z += B // 100
      B %= 100
  
      p(f"${Z}.{B:02d}")  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
