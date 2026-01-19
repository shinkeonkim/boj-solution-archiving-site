import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def solve():
  n = ii()
  
  l = [inp() for _ in range(n)]
  
  ans = []
  
  for i in range(n):
    if l[i] == 'Present!':
      continue
    
    if i + 1 == n:
      ans.append(l[i])
      continue

    if l[i + 1] != 'Present!':
      ans.append(l[i])
      
  if len(ans) == 0:
    print("No Absences")
  else:
    print(*ans, sep="\n")
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    