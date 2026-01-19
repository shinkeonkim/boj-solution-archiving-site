import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n = int(input())

  x = n - 2

  print("|" + x * "-" + "|")

  for i in range(n // 2 - 1):
    print("|" + BLANK * i + "*" + BLANK * (x - 2 * (i + 1)) + "*" + BLANK * i + "|")

  print("|" + BLANK * (n // 2 - 1) + "*" +  BLANK *  (n // 2 - 1) + "|")

  for i in range(n // 2 - 2, -1, -1):
    print("|" + BLANK * i + "*" + BLANK * (x - 2 * (i + 1)) + "*" + BLANK * i + "|")
  print("|" + x * "-", end="|")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()