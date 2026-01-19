x, y = map(int, input().split())
x, y = bin(x)[2:][::-1], bin(y)[2:][::-1]

ans = ""
for i in range(max(len(x), len(y))):
  ans += y[i] if i < len(y) else "0"
  ans += x[i] if i < len(x) else "0"

print(int(ans[::-1], 2))
