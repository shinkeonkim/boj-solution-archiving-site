import sys
input = sys.stdin.readline

ans = 1
n = int(input())
k = int(input())
l = [*map(int, input().split())]
for i in l:
  if i > k:
    ans += 1
print(ans)