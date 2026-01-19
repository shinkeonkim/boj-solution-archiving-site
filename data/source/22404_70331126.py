import sys

input = sys.stdin.readline

n, m, t = map(int, input().split())
l = [*map(int, input().split())]

ans = l[0] - m

for i in range(1, n):
  if l[i] - l[i - 1] >= 2 * m:
    ans += l[i] - l[i - 1] - 2 * m

if t - l[n - 1] >= m:
  ans += t - l[n - 1] - m
  
print(ans)