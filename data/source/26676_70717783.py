import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


n = ii()
l = sorted(input().split())
chk = True

for i in range(1, 5):
  for j in range(3):
    k = str(i)+chr(j + 65)
    if l.count(k) < 1:
      chk = False

for j in range(3):
  k = "5"+chr(j + 65)
  if l.count(k) < 2:
    chk = False
    
print("TAK" if chk else "NIE")