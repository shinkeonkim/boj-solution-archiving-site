n, k, a = map(int, input().split())
l = [[*map(int, input().split())] for i in range(n)]

times = []
drinking_time = k // a

for t, s in l:
  if drinking_time % t == 0:
    d = drinking_time // t - 1
    times.append(drinking_time + d * s)
  else:
    d = drinking_time // t 
    times.append(drinking_time + d * s)
print(min(times))
