import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l, a):
  ret = []
  
  for i in l:
    ret.append(i * a)
    ret.append(i + a)
    ret.append(i - a)
    
    if a != 0 and i % a == 0:
      ret.append(i // a)
  return ret


def solve():
  a, b, c = mii()
  
  k = f([a], b)
  k = f(k, c)
  
  ans = 1111111111111111
  for i in k:
    if i >= 0 and i < ans:
      ans = i
  print(ans)

  
  
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()
