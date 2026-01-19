import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  l = input().split()

  for i in range(4):
    for j in range(3):
      if int(l[j] + l[j + 1]) <= int(l[j + 1] + l[j]):
        l[j], l[j+1] = l[j+1], l[j]
  print(*l, sep="")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()