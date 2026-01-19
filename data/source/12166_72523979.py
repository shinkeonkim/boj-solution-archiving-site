import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s, k):
  ret = ""

  for i in s:
    ret += chr((ord(i) - 97 - k + 26) % 26 + 97)

  if "i" in ret:
    return 0
  return 1

def solve():
  n, s = input().split()
  n = int(n)
  s = [*map(int, list(s))]

  ret = 0
  crt = s[0]

  for i in range(1, n + 1):
    if crt < i and s[i] > 0:
      ret += i - crt
      crt += i - crt
    crt += s[i]

  return ret

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")