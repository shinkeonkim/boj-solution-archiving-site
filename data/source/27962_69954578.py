def f(a, b):
  cnt = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      cnt += 1
  return cnt == 1

n = int(input())
s = input()

for i in range(1, n+1):
  if f(s[:i], s[-i:n]):
    print("YES")
    break
else:
  print("NO")