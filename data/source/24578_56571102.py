l = [*map(int, list(input()))]

s = 8
while s > 0:
  for i in range(4):
    if l[i] >= s:
      l[i] -= s
      print(end="*")
    else:
      print(end=".")
    if i == 0 or i == 2:
      print(end=" ")
    elif i == 1:
      print(end=" " * 3)
    else:
      print()

  s //= 2