d = [1, 5, 10, 20, 50, 100]
l = [*map(int, input().split())]
k = [d[i] * l[i] for i in range(6)]

idx = 0
mx = k[0]
for i in range(1, 6):
  if mx < k[i]:
    mx = k[i]
    idx = i
  elif mx == k[i] and l[idx] > l[i]:
    idx = i
print(d[idx])
