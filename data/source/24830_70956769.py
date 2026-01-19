import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  prev = 1
  
  for i in range(ii()):
    a, b, c = input().split()
    a = int(a)
    c = int(c)
    
    crt = 0
    if b == "*":
      crt = (a * c) ** 2
    elif b == "+":
      crt = a + c - prev
    elif b == "-":
      crt = (a - c) * prev
    else:
      crt = (a + 1) // 2
    prev = crt
    print(crt)
      
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
