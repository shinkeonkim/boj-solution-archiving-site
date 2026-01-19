def f(a):
  d = [60, 100, 140, 200, 250, 100000]
  
  for i in range(6):
    if a < d[i]:
      return i

l = sorted([int(input()) for i in range(int(input()))], reverse=True)[:42]

a_sum = sum([f(i) for i in l])

print(sum(l), a_sum)
