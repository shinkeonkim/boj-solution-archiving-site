import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    l = mii()
    if len(l) == 1:
      break
    n, *l = l
    
    s = sum(l)
    
    k = 0
    for idx in range(n):
      k += l[idx]
      
      if k * 2 == s:
        print(f"Sam stops at position {idx + 1} and Ella stops at position {idx + 2}.")
        break
    else:
      print("No equal partitioning.")
  
if __name__ == "__main__":
  tc = 1
  
  
  for t in range(1, tc+1):
    ret = solve()
