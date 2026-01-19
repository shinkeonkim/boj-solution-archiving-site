n = int(input())
l = [int(input()) for i in range(n)]

s = l[-1]
l = l[:-1]

last = (sum(l) - s) // (n - 2)

for i in l:
  print(i - last)
print(last)
