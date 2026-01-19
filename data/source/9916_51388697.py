n = int(input())

ans = 0
t = 1

for i in range(2, n + 1):
    t *= i
    
    while t % 10 == 0:
        t //= 10
        ans += 1
    
while t > 0:
    if t % 10 == 0:
        ans += 1
    t //= 10

print(ans)
