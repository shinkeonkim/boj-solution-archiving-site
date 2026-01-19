import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    m, n = mii()
    if m == n == 0:
      break

    l = [2 for i in range(5001)]

    for i in range(2, 5001):
      for j in range(i + i, 5001, i):
        l[j] += 1

    Y = X = 0
    for i in range(n, m - 1, -1):
      if Y < l[i]:
        Y = l[i]
        X = i
    p(X, Y)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
