n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
k = int(input())

chk = [0] * 32

for s, e in l:
  for j in range(s, e):
    chk[j] += 1

print(int(max(chk) <= k))