n = int(input())

d = 1
for i in range(1, n):
    d += 1

    if "50" in str(i):
        d += 1

print(d)
