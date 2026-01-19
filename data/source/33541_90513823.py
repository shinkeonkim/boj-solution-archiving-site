n = int(input())

for i in range(n + 1, 10000):
  a, b = i // 100, i % 100

  if (a + b) ** 2 == i:
    print(i)
    break
else:
  print(-1)
