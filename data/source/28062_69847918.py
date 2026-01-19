n = int(input())
l = [*map(int, input().split())]

s = 0
odd = []

for i in l:
  if i % 2:
    odd.append(i)
  else:
    s += i

odd.sort(reverse = True)

for i in range(1, len(odd), 2):
  s += odd[i - 1] + odd[i]
  
print(s)