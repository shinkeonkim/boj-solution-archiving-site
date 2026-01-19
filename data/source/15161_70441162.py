import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

A = {}
B = {}
n = ii()
L = [[n + 1] * 10 for i in range(10)]
l = [mii() for _ in range(n)]

for T in range(n - 1, - 1, -1):  
  for i in range(3):
    for j in range(0, 10):
      L[l[T][i] - 1][j] = min(n - T, L[l[T][i] - 1][j]) 
      L[j][l[T][i + 3] - 1] = min(n - T, L[j][l[T][i + 3] - 1])

for i in range(10):
  print(*L[i])
