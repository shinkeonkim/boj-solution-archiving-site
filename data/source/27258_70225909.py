import sys

input = sys.stdin.readline

def gcd(a, b):
  return gcd(b, a % b) if b else a

n, p, q = map(int, input().split())
ans = []
for a in range(1, n + 1):
  for b in range(a + 1, n + 1):
    if gcd(a, b) != 1:
      continue
    
    if b >= a * p or a * q >= b:
      continue
    ans.append([a, b])

    
ans.sort(key = lambda t: (t[0] / t[1]))

for a, b in ans:
  print(f"{a}/{b}")
