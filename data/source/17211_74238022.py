import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def multiply(a, b):
  ret = [[0] * 2 for _ in range(2)]
  
  ret[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
  ret[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
  ret[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
  ret[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]

  return ret


def mul(l, n):
  matrix = l[::]
  if n == 1:
    return matrix
  
  if n == 2:
    return multiply(matrix[::], matrix[::])

  k = mul(matrix[::], n // 2)

  if n % 2 == 0:
    return multiply(k, k)
  else:
    return multiply(multiply(k, k), matrix[::])
  
    
def solve():
  n, k = mii()
  l = mfi()
  
  l = [[l[0], l[1]], [l[2], l[3]]]
  
  ret = mul(l[::], n)
  
  for i in range(2):
    p(int(ret[k][i] * 1000))

      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
