import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def solve():
  s = inp()
  prev = '('
  l = [0]
  n = len(s)
  
  for i in range(1, n):
    crt = s[i]
    
    if crt == prev:
      l.append(l[-1] + (1 if crt == '(' else -1))
    else:
      l.append(l[-1])
    prev = crt

  m = max(l)
  
  for i in range(m, -1, -1):
    for j in range(n):
      if l[j] == i:
        print(end=('/' if s[j] == '(' else '\\'))
      else:
        print(end=".")
    print()

if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    