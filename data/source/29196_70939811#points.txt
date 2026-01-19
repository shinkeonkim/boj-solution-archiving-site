import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  _, p = input().split(".")
  q = 10 ** 9
  print("YES")
  print(int(p) * (10 ** (9 - len(p))), q)
  
        
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()

    