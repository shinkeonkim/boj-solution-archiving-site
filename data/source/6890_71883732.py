import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  key = input()
  n = len(key)

  s = input()

  ans = ""

  j = 0
  for i in s:
    if 'A' <= i <= 'Z':
      k = ord(key[j % n]) - 65

      ans += chr((ord(i) - 65 + k) % 26 + 65)
      j += 1

  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()