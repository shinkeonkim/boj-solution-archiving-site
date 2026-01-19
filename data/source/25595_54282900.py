n = int(input())
l = [[*map(int, input().split())] for i in range(n)]

t = 0
s = set()

for i in range(n):
  for j in range(n):
    if l[i][j] == 2:
      t = (i + j) % 2
    elif l[i][j] == 1:
      s.add((i + j) % 2)
s = list(s)
print('Kiriya' if len(s) == 2 or (len(s) == 1 and s[0] == t) else 'Lena')