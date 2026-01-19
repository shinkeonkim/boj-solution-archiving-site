import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solve():
  while 1:
    d, n = input().split()
    d = float(d)
    n = int(n)
    
    if n == 0:
      break

    chk = [False] * n

    l = [mfi() for _ in range(n)]

    for i in range(n):
      for j in range(i + 1, n):
        if dis(l[i], l[j]) <= d * d:
          chk[i] = True
          chk[j] = True
    
    cnt = chk.count(True)
    
    print(f"{cnt} sour, {n-cnt} sweet")
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

