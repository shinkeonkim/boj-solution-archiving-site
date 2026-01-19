import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def f(a, b):
  if a[0] == -1:
    if b[2] != -1 and b[1] != -1 and b[2] - b[1] >= 0:
      a[0] = b[2] - b[1]
  
  if a[1] == -1:
    if a[2] != -1 and b[0] != -1 and a[2] - b[0] >= 0:
      a[1] = a[2] - b[0]
  
  if a[2] == -1:
    if a[1] != -1 and b[0] != -1:
      a[2] = a[1] + b[0]
      
  if a[2] == 0:
    a[1] = 0

  return a
def solve():
  a = mii()
  b = mii()
  
  for _ in range(100):
    a = f(a, b)
    b = f(b, a)
  
  print(*a)
  print(*b)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    