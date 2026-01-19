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
    s, crt = input().split()
    crt = int(crt)

    if s == "#" and crt == 0:
      break

    while 1:
      flag, k = input().split()
      k = int(k)

      if flag == "X" and k == 0:
        break

      if flag == "B":
        if crt + k <= 68:
          crt += k
      else:
        if crt - k >= 0:
          crt -= k
    print(s, crt)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()