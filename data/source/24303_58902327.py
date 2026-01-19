MX = 10000000000
a, b, c, x, y, z, l = map(int, input().split())
ans = MX

for i in range(0, x+1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            l2 = a * i + b * j + c * k
            
            if l2 >= l and i + j + k < ans:
                ans = i + j + k

print(0 if ans == MX else ans)