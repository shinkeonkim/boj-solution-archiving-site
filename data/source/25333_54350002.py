def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a

for i in range(int(input())):
  a, b, x = map(int, input().split())
  print(x // gcd(a, b))
