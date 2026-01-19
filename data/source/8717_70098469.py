n = int(input())
l = [*map(int, input().split())]

s = sum(l)
crt = 0
mn = 10000000000000

for i in l[:-1]:
  crt += i
  
  mn = min(mn, abs(crt - (s - crt)))
  
print(mn)
