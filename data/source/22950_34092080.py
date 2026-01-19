n = int(input())
s = input()
k = int(input())

for i in range(max(-k, -n), 0, 1):
  if s[i] == '1':
    print("NO")
    break
else:
  print("YES")