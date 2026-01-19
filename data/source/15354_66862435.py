d = 1
n = int(input())
l = [input() for i in range(n)]

for i in range(1, n):
    if l[i-1] != l[i]:
        d += 1

print(d + 1)