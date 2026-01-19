import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  name = ["Lab", "Hw", "Proj", "Exam"]
  *total, n = mii()
  
  d = {}
  A = {}
  B = {}
  
  for i in range(4):
    d[name[i]] = total[i]
  
  ans = 0
  for _ in range(n):
    s = input()
    
    cat, score = s.split(": ")
    
    cat = cat.split(" ")[0]
    a, b = map(int, score.split("/"))
    A[cat] = A.get(cat, 0) + a
    B[cat] = B.get(cat, 0) + b
  
  for key in name:
    if key not in A:
      continue
    ans += (A[key] / B[key]) * d[key]
  
  p(int(ans))
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

