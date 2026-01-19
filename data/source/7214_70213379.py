import sys
input = sys.stdin.readline

k, s = map(int, input().split())
l = [*map(int, input().split())]
ans = 0

for i in l:
  ans += min(k - 1, i)

print(ans + 1)