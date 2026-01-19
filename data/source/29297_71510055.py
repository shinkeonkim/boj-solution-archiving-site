import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  A = 0
  B = 0
  C = 0
  for i in range(10):
    for j in range(10):
      if a + i > b + j:
        A += 1
      elif a + i < b + j:
        B += 1
      else:
        if i > b:
          A += 1
        elif i < b:
          B += 1
        else:
          C += 1
        
  p(A, B)
  
def solve():
  a, b = mii(":")
  f(a, b)
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
    
