import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f1(s):
  # 특수문자
  for i in "#@*&":
    if i in s:
      return s
  
  return s + "#"

def f2(s):
  # 영어 대문자
  for i in s:
    if 'A' <= i <= 'Z':
      return s
  return s + 'A'

def f3(s):
  # 영어 소문자
  for i in s:
    if 'a' <= i <= 'z':
      return s
  return s + 'a'

def f4(s):
  # 숫자
  for i in s:
    if '0' <= i <= '9':
      return s
  return s + '0'
  
def f5(s):
  # 길이
  ln = max(7 - len(s), 0)
  
  return s + "0" * ln

def solve():
  n = ii()
  s = input()
  
  s = f1(s)
  s = f2(s)
  s = f3(s)
  s = f4(s)
  s = f5(s)
  
  return s
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")
