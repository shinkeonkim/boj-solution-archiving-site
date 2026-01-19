import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l, n):
  for i in l:
    if i != i[::-1]:
      return False
  return True

def g(l, n):
  l2 = []

  for i in range(n):
    _l2=[]
    for j in range(n):
      _l2.append(l[j][i])
    l2.append(_l2)
  return f(l2, n)
  
def solve():
  n = ii()
  l = [input() for _ in range(n)]
  
  a = f(l, n)
  b = g(l, n)
  
  if a and b:
    p("Magnificent")
  elif a:
    p("Graceful")
  elif b:
    p("Beautiful")
  else:
    p("Useless")
        
if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    solve()

    