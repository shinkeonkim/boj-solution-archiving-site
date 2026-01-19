input()
s = input()

crt = 1
ans = 0
for i in s:
  if i == 'L':
    crt -= 1
  
  if i == 'R':
    crt += 1
  
  if crt == 0:
    crt = 1
  
  if crt == 4:
    crt = 3
  
  if crt == 3:
    ans += 1

print(ans)