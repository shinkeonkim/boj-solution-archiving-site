n = int(input())
l = [*map(int,input().split())]

d = {}
for i in l:
  try:
    d[i] += 1
  except:
    d[i] = 1

print(sorted(d.items(), key=lambda t : (t[1], t[0]))[0][0])
