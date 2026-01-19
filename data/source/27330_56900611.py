n = int(input())
l = [*map(int, input().split())]
m = int(input())
l2 = [*map(int, input().split())]

s = 0
for i in l:
  s += i
  
  if s in l2:
    s = 0
print(s)