import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

A = 0

for a in range(1, 10):
  # A가 a인지 물어보고 flush를 한다.
  # print에 flush 파라미터를 넣으면 된다.
  print("? A", a, flush=True)

  # 채점기의 답변을 입력받는다.
  resp = int(input())

  if resp == 1:
    A = a
    break

for b in range(1, 10):
  print("? B", b, flush=True)

  # 채점기의 답변을 입력받는다.
  resp = int(input())

  if resp == 1:
    B = b
    break

print("!", A + B)