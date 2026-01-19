l = [*map(int, input().split())]

for n in l:
  for i in range(1, n + 1):
    if i == n:
      print(" " * (n - 1) + "*")
    else:
      print(" " * (i - 1) + "*" + " " * ((n - i) * 2 - 1) + "*")
      