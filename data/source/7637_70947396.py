import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def g(a):
  s1, e1 = a.split("-")
  x = [*map(int, s1.split(":"))]
  y = [*map(int, e1.split(":"))]
  
  return [x[0] * 60 + x[1], y[0] * 60 + y[1]]

def f(a, b):
  a = g(a)
  b = g(b)
  
  if b[1] <= a[0] or a[1] <= b[0]:
    return False
  
  return True

def solve():
  while 1:
    n = ii()

    if n == 0:
      break
    
    l = [input() for _ in range(n)]
    
    chk = False
    for i in range(n):
      for j in range(i + 1, n):
        if f(l[i], l[j]):
          print("conflict")
          chk = True
          break
      if chk:        
        break
    else:
      print("no conflict")
  
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
