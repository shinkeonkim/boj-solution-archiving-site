def f(s):
  d = {}
  for i in s:
    try:
      d[i] += 1
    except:
      d[i] = 1
  return sum(sorted(d.values())[:-2])

for i in range(int(input())):
  print(f(input()))