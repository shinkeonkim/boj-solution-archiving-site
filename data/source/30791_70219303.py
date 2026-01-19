import sys
input = sys.stdin.readline

l = [*map(int, input().split())]
ans = 0
for i in range(1, 5):
  if l[0] - l[i] <= 1000:
    ans += 1
print(ans)