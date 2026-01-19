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

def f(a, crt):
  a = "".join(a)
  crt = "".join(crt)
  for i in range(len(a)):
    if a[i] == '.' and crt[i] == 'x':
      return False
  return True

def solve():
  h, w, n = mii()
  
  l = []
  
  for i in range(n):
    l.append([input() for j in range(h)])
  
  crt = [input() for j in range(h)]
  
  cnt = 0
  
  for i in range(n):
    if f(l[i], crt):
      cnt += 1
  if cnt == 1:
    p("yes")
  else:
    p("no")
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
