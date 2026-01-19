def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a

def lcm(a, b):
  return a * b // gcd(a, b)

n = int(input())
l = [*map(int, input().split())]

p = l[0]

for i in range(1, n):
  p = lcm(p, l[i])

c = 0

for i in range(n):
  c += p // l[i]

tmp = gcd(p, c)
p //= tmp
c //= tmp

print(f"{p}/{c}")
