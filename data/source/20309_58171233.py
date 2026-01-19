n = int(input())
l = [0] + [*map(int, input().split())]

for i in range(1, n + 1):
    d = abs(i - l[i])
    
    if d % 2 == 1:
        print("NO")
        break
else:
    print("YES")