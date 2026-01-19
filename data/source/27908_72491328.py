import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(n):
  if n < 10:
    return ".." + str(n)
  return "." + str(n) 
  
def solve():
  n, start = mii()
  
  start -= 1

  end_condition = (((n + start) // 7 + int((n + start) % 7 > 0)) * 7)
  
  print("+" + "-" * 21 + "+")
  
  i = 0
  crt = 1
  while i < end_condition:
    if i % 7 == 0:
      print(end="|")
    
    if i % 7 == start % 7 and crt <= n:
      start += 1
      print(end=f(crt))
      crt += 1
    else:
      print(end="...")
    
    if i % 7 == 6:
      print("|")
    i += 1
  print("+" + "-" * 21 + "+")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
        
