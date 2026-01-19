import sys

N, K = map(int, input().split())
l = [int(sys.stdin.readline()) for i in range(K)]

d = [0] * (N + 1)

for i in l:
  d[i] = 1

d[1] = 1
for i in range(2, N + 1):
  if d[i - 1] == 0 and d[i] == 0:
    d[i] = 1

print(sum(d))