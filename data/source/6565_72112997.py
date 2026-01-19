import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a):
  return int(a[::-1])

def solve():
  while 1:
    s = input()
    
    if s == "0+0=0":
      p("True")
      break
    
    a, c = s.split("=")
    a, b = a.split("+")
    
    a = f(a)
    b = f(b)
    c = f(c)
    
    if a + b == c:
      p("True")
    else:
      p("False")
    
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

