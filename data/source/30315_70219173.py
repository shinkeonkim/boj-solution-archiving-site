import sys
from math import sqrt
input = sys.stdin.readline


def dis(a, b):
  return sqrt((a[0] - b[0]) ** 2 + ((a[1] - b[1]) ** 2))

n = int(input())
l = [[*map(int, input().split())] for i in range(n)]

ans = 1000000000

for i in range(0, n):
  crt = 0
  
  for j in range(0, n):
    if i == j:
      continue
    crt += dis(l[i], l[j])

  ans = min(ans, crt / (n - 1))

print(ans)