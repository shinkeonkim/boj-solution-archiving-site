import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
s = inp()

B = s.count("B")
S = s.count("S")
A = s.count("A")

if B == S == A:
  print("SCU")
else:
  m = max([B, S, A])
  
  if B == m:
    print(end="B")
  if S == m:
    print(end="S")
  if A == m:
    print(end="A")