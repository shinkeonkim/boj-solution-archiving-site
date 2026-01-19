n = int(input())
l = [*map(int, input().split())]

a, b = 0, 0

for i in l:
  if i < 0:
    a += 1
  else:
    b += 1

print(a * b + (a * (a - 1)))