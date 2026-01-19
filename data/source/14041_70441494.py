import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

h, m = mii(":")
crt = h * 60 + m
k = 0

i = 0
while i < 120:
  if 420 <= crt < 600:
    crt += 2
  elif 900 <= crt < 1140:
    crt += 2
  else:
    crt += 1
  i += 1
  
print("{:02d}:{:02d}".format((crt // 60) % 24, crt % 60))