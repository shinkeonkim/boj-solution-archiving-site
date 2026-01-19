import sys

input = sys.stdin.readline

n = int(input())
l = [*map(int, input().split())]

while (len(l) != n):
  try:
    l2 = [*map(int, input().split())]
    l.extend(l2)
  except:
    break
ans = 0
cnt = 0
mn = 11111111

for i in l:
  if i % 2 == 1:
    cnt += 1
    if mn > i:
      mn = i
  ans += i

if cnt % 2 == 1:
  ans -= mn

print(ans // 2)
