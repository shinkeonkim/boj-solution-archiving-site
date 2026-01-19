import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  if a == 1 and b == 2:
    return 200
  if a == 2 and b == 1:
    return 200
  
  if a == b:
    return 100 + a
  
  return max(a, b) * 10 + min(a, b)



def solve():
  while 1:
    a, b, c, d = mii()
    if a == b == c == d == 0:
      break
    
    A = f(a, b)
    B = f(c, d)
    
    if A > B:
      p("Player 1 wins.")
    elif A < B:
      p("Player 2 wins.")
    else:
      p("Tie.")
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
