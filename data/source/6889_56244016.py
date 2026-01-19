n = int(input())
m = int(input())

x = [input() for i in range(n)]
y = [input() for i in range(m)]

for i in range(n):
  for j in range(m):
    print(f"{x[i]} as {y[j]}")
