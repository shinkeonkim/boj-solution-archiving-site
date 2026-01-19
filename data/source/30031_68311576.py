d = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
s = 0
for _ in range(int(input())):
  a, b = map(int, input().split())
  s += d[a]
print(s)