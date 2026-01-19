import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

def f(l):
  k = l[1] - l[0]
  for i in range(2, 4):
    if l[i] - l[i - 1] != k:
      return False
  return True

def g(l):
  for i in range(2, 4):
    if l[i] * l[0] != l[1] * l[i - 1]:
      return False
  return True

while 1:
  l = mii()
  
  if sum(l) == -4:
    break
  
  
  for i in range(1, 20000):
    l2 = []
    
    for j in l:
      if j == -1:
        l2.append(i)
      else:
        l2.append(j)

    if f(l2) or g(l2):
      print(i)
      break
  else:
    print(-1)
