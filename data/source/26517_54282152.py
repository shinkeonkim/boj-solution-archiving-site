k = int(input())
a, b, c, d = map(int, input().split())

x = a * k + b
y = c * k + d

if x == y:
  print('Yes', x)
else:
  print('No')
