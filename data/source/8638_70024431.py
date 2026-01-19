n = int(input())
l = [*map(int, input().split())]
mx = max(l)

for i in range(n):
  if l[i] == mx:
    print(end=chr(65 + i))
