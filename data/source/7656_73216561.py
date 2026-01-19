import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  s = s.replace("What is", "Forty-two is")
  s += "."
  
  p(s)

def solve():
  s = input()
  crt = ""
  for i in s:
    if i == '?':
      f(crt)
      crt = ""
    elif i == '.':
      crt = ""
    else:
      crt += i
    
    if crt == " ":
      crt = ""
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
