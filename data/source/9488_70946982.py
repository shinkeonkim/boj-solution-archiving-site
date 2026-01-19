import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = [0, 1]
  
  for i in range(2, 1000001):
    l.append(l[-1] + i * (i + 1) // 2)
  
  k = sys.stdin.readlines()
  
  for n in k:
    n = int(n.strip())
    if n == 0:
      break
    sys.stdout.write(str(l[n])+"\n")
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
