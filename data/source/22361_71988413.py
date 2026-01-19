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
    n, m = mii()

    if n == m == 0:
      break

    a = mii()
    b = mii()

    d = [0] * 10
    for i in a:
      for j in b:
        k = i * j

        for s in str(k):
          d[int(s)] += 1

    print(*d)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()