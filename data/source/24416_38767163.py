l = [0, 1, 1]

for i in range(3, 44):
  l.append(l[-1]+l[-2])

n = int(input())
print(l[n], n-2)
