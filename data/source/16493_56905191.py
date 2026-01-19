n, m = map(int, input().split())

l = [[*map(int, input().split())] for i in range(m)]
D = [0] * (n + 1)

for i in range(m):
  cost = l[i][0]
  value = l[i][1]
  
  for j in range(n, -1, -1):
    if (j == 0 or D[j] > 0) and j + cost <= n:
      D[j + cost] = max(D[j + cost], D[j] + value)
print(max(D))
