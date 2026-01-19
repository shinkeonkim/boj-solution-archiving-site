import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  a, b = map(int, s.split())
  return a * b

def solve():
  n = ii() # 패턴의 이미지 수
  
  l = sum([f(input()) for _ in range(n)])
  # S: 평방 인치, R: 세트에 포함된 이미지 수

  #1제곱 야드 -> 1야드는 36인치 36 * 36
  #2제곱 야드 -> 36 * 36 * 2
  #3제곱 야드 
  
  k = 36 * 36
  
  for i in range(1, 4):
    p(k * i // l, end = " ")
  p()
  
tc = ii()

for t in range(1, tc+1):
  ret = solve()
    