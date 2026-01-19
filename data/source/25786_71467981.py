a = input()
b = input()

n = max(len(a), len(b))

a = "0" * (n - len(a)) + a
b = "0" * (n - len(b)) + b
ans = ""
for i in range(n):
  x = int(a[i])
  y = int(b[i])

  if (x <= 2 and y <= 2) or (x >= 7 and y >= 7):
    ans += "0"
  else:
    ans += "9"
print(ans)