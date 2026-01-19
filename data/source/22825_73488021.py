import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(num, l):
  for oper, k in l:
    k = int(k)
    
    if oper == "ADD":
      num += k
    elif oper == "SUBTRACT":
      num -= k
      
      if num < 0:
        return 1
    elif oper == "MULTIPLY":
      num *= k
    else:
      if num % k > 0:
        return 1
      num //= k
  return 0


def solve():
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    l = [i** 3 for i in range(2000)]
    
    ans = n ** 3
    
    for i in range(1, n):
      for j in range(1, n):
        k = l[i] + l[j]
        
        if k > n ** 3:
          break
        
        ans = min(ans, n ** 3 - k)
    
    p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
