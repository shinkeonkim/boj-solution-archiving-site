d = {}
for i in range(1, 13):
  d[i] = 0

for i in range(int(input())):
  _, s = input().split()
  _, m, __ = s.split("/")
  
  d[int(m)] += 1

for i in range(1, 13):
  print(i, d[i])
  