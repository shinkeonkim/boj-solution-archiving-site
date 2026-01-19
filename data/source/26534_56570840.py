a = [*map(int, input().split())]
b = [*map(int, input().split())]

cnt = 0
s = 0
for i in a:
  for j in b:
    if i > j:
      cnt += 1
    if i == j:
      s += 1
print(f"{cnt / (36 - s):.5f}")