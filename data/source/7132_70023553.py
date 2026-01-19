def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a

n, m = map(int, input().split())

s = set()

for i in range(n, m + 1):
  for j in range(n, m + 1):
    g = gcd(i, j)
    
    s.add(i // g * 1000 + j // g)

print(len(s))