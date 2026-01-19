d = {
  "N": (1, 0),
  "S": (-1, 0),
  "E": (0, 1),
  "W": (0, -1),
}

input()
a, b = 0, 0
s = input()

for i in s:
  a += d[i][0]
  b += d[i][1]
print(abs(a) + abs(b))