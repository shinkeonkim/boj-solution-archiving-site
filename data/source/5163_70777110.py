import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def v(r):
  return 4 / 3 * pi * (r ** 3)

def solve():
  b, w = input().split()
  b = int(b)
  w = float(w)
  
  v_sum = [v(float(input())) for _ in range(b)]
  
  if w <= sum(v_sum) / 1000:
    print("Yes")
  else:
    print("No")
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(tc):
    print(f"Data Set {t+1}:")
    solve()
    print()
    