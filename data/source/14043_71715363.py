import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a = input()
  b = input()
  
  k = b.count("*")
  b = b.replace("*", "")
  
  a = sorted(list(a))
  b = sorted(list(b))
      
  i = j = 0
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      i += 1
      j += 1
    else:
      k -= 1
      i += 1
    
  k -= len(a) - i
  
  if k >= 0:
    return "A"
  return "N"
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
