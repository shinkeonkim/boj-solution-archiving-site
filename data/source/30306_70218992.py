a = b = 0

n = int(input())
x = [*map(int, input().split())]
y = [*map(int, input().split())]

for i in range(n):
  for j in range(n):
    if x[i] > y[j]:
      a += 1
    elif x[i] < y[j]:
      b += 1
if a > b:
  print("first")
elif a < b:
  print("second")
else:
  print("tie")