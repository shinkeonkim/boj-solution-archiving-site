import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())

for _ in range(ii()):
  a = mfi()
  b = mfi()
  
  # 0: 보, 1: 바위, 2: 가위
  # A: 가위-보, 바위-가위, 보-바위
  x = a[2] * b[0] + a[1] * b[2] + a[0] * b[1]
  y = b[2] * a[0] + b[1] * a[2] + b[0] * a[1]
  
  if abs(x - y) <= 0.0000001:
    print("=")
  elif x < y:
    print("GOSIA")
  else:
    print("ADAM")