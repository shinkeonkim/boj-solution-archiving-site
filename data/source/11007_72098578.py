import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  chk = [i for i in range(26)]
  
  n = ii()
  l = mii()
  
  ans = []
  
  for crt in l:
    ans.append(chk[crt])
    
    chk = [chk[crt]] + chk[:crt] + chk[crt+1:]
  for i in ans:
    print(end=chr(97+i))
  print()
    
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
