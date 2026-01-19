import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l):
  ret = []
  for j in range(6):
    d = 0
    for i in range(4):
      d *= 2
      d += l[i][j]
    ret.append(d)
  
  ret2 = []
  
  for i in range(3):
    ret2.append(ret[i * 2] * 10 + ret[i * 2 + 1])
  
  return tm_set(ret2)


def tm_set(tm):
  tm[1] += tm[2] // 60
  tm[2] %= 60
  
  tm[0] += tm[1] // 60
  tm[1] %= 60
  
  tm[0] %= 24
  
  return tm

def num_to_ar(num):
  d = 8
  r = []
  while d > 0:
    if num >= d:
      r.append(1)
      num -= d
    else:
      r.append(0)

    d //= 2
  return r

def solve():
  a = [mii() for _ in range(4)]
  b = [mii() for _ in range(4)]
  
  a = f(a)
  b = f(b)
  
  c = [a[i] + b[i] for i in range(3)]
  c = tm_set(c)
  
  l = []
  
  for i in c:
    l.append(num_to_ar(i // 10))
    l.append(num_to_ar(i % 10))

  # p(a, b, c, l)
  for j in range(4):
    for i in range(6):
      p(l[i][j], end = " ")
    p()
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
