s = input()
n = len(s) // 3

for i in range(n):
  tmp = sorted([s[i], s[n+i], s[2*n+i]])
  print(tmp[0] if tmp[0] == tmp[1] else tmp[1], end="")
