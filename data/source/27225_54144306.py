a = int(input())
b = int(input())

s = min(a, b)
s2 = max(a - s, b - s)

s *= 2
if s2 % 2:
  s += 1

print(s)
