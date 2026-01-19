d = {
  "STRAWBERRY": 0,
  "BANANA": 0,
  "LIME": 0,
  "PLUM": 0,
}

for i in range(int(input())):
  s, n = input().split()
  d[s] += int(n)

print("YES" if 5 in d.values() else "NO")
