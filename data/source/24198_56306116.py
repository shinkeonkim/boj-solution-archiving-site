l = [0, 0]
n = int(input())

turn = 1
while n > 0:
  l[turn] += n // 2 + n % 2 
  n = n // 2
  
  turn = 1 - turn

print(*l)