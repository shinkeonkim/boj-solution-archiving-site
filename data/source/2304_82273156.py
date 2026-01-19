"""
[2304: 창고 다각형](https://www.acmicpc.net/problem/2304)

Tier: Silver 2 
Category: bruteforcing, data_structures, stack
N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
지붕의 가장자리는 땅에 닿아야 한다.
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
그림 1은 창고를 옆에서 본 모습을 그린 것이다. 이 그림에서 굵은 선으로 표시된 부분이 지붕에 해당되고, 지붕과 땅으로 둘러싸인 다각형이 창고를 옆에서 본 모습이다. 이 다각형을 창고 다각형이라고 하자.



그림1 . 기둥과 지붕(굵은 선)의 예

창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다. 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.

기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

입력
첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. L과 H는 둘 다 1 이상 1,000 이하이다.

출력
첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.

예제 입력 1 
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
예제 출력 1 
98
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  n = ii()
  l = [mii() for _ in range(n)] # 각 기둥의 위치와 높이
  
  l.sort() # 위치 순으로 정렬
  
  # 왼쪽에서 오른쪽으로 가면서 가장 높은 기둥을 찾는다.
  mx_idx = 0
  for i in range(n):
    if l[i][1] > l[mx_idx][1]:
      mx_idx = i
  
  # 왼쪽에서 가장 높은 기둥까지의 면적을 구한다.
  
  area = 0
  h = l[0][1]
  for crt in range(1, mx_idx+1):
    if crt > 0:
      area += h * (l[crt][0] - l[crt-1][0])

    if l[crt][1] > h:
      h = l[crt][1]
    
  h = l[n-1][1]
  for crt in range(n-2, mx_idx-1, -1):
    if crt + 1 < n:
      area += h * (l[crt+1][0] - l[crt][0])

    if l[crt][1] > h:
      h = l[crt][1]
    
  
  p(area + l[mx_idx][1])
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()