import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  r, c = mii()

  print(".."+"+-"*(c - 1)+"+")
  print(".."+"|."*(c - 1)+"|")
  for i in range(r - 1):
    print("+-"*c+"+")
    print("|."*c+"|")
  print("+-"*c+"+")

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    print(f"Case #{t}:")
    ret = solve()