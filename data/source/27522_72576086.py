import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  t, team = s.split()
  m, s, ss = map(int, t.split(":"))
  tm = ss + s * 1000 + m * 60000
  return (tm, team)

def solve():
  table = [10, 8, 6, 5, 4, 3, 2, 1]

  l = [f(input()) for _ in range(8)]

  l.sort(key = lambda t : t[0])

  score = {
    "B": 0,
    "R": 0,
  }
  for i in range(8):
    score[l[i][1]] += table[i]

  if score["B"] > score["R"]:
    p("Blue")
  else:
    p("Red")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()