n = int(input())
l = [*map(int, input().split())]

l_0 = l_1 = r_0 = r_1 = 0

for i in range(0, n):
  if l[i] == 0:
    l_0 = i
    break

for i in range(0, n):
  if l[i] == 1:
    l_1 = i
    break
    
for i in range(n - 1, -1, -1):
  if l[i] == 0:
    r_0 = i
    break
    
for i in range(n - 1, -1, -1):
  if l[i] == 1:
    r_1 = i
    break

print(max([abs(l_0 - r_1), abs(l_0 - l_1), abs(r_0 - l_1), abs(r_0 - r_1)]))