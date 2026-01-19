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
    n = input()
    if n == "0":
      break
      
    n = [*map(int, list(n))]
    m = max(n)
    idx = -1
    
    for i in range(len(n)):
      if n[i] == m:
        idx = i
        break
    
    if n[idx] % 2:
      n[idx] = 0
    else:
      n[idx] = (n[idx] + 4) % 10
    
    p(int("".join([*map(str, n)])))
    
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()

    