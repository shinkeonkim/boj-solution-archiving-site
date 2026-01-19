from sys import exit

n, m, k = map(int, input().split())

if n + m - 1 > k:
    print("NO")
    exit()
print("YES")
for i in range(1, n + 1):
    for j in range(0, m):
        print(i + j, end=" ")
    print()