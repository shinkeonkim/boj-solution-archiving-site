a, b, c = map(int, input().split())

a = abs(a)
b = abs(b)

if a + b == 0:
  print("YES" if c % 2 == 0 else "NO")
else:
  print("YES" if a + b <= c and (c - (a + b)) % 2 == 0 else "NO")
