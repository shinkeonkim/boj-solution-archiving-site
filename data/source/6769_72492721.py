import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  s = input()

  ans = 0

  crt = 0
  l = []
  for i in s:
    if '0' <= i <= '9':
      crt *= 10
      crt += int(i)
    else:
      l.append([d[i], crt])

      crt = 0

  for i in range(0, len(l)):
    if i + 1 < len(l):
      if l[i + 1][0] > l[i][0]:
        ans -= l[i][0] * l[i][1]
        continue
    ans += l[i][0] * l[i][1]

  print(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()