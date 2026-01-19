import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(x, y):
  return x * 10 + y

def g(a, b):
  if a > b:
    return (b, a)
  return (a, b)

def solve():
  X = mii()
  
  W, H = g(f(X[0], X[1]), f(X[2], X[3]))
  
  l = [mii() for _ in range(2)]
  
  ans = -1
  mn = 11111111111111111111111
  
  for i in range(2):
    a, b, c, d = l[i]
    
    w, h = g(f(a, b), f(c, d))
  
    if w >= W + 10 and h >= H and mn > w:
      ans = [w, h, i]
      mn = w
  if ans == -1:
    print(0)
    return
  
  print(ans[2] + 1)
  print(f"{ans[0]//10}.{ans[0]%10} {ans[1]//10}.{ans[1]%10}")
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
