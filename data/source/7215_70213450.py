import sys
input = sys.stdin.readline

k, s = map(int, input().split())
l = [*map(int, input().split())]
ans = 0
cnt = 0

for i in l:
  if i < k:
    cnt += 1
  ans += min(k - 1, i)

print(-1 if cnt == s else ans + 1)
