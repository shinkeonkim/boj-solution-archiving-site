n = int(input())
l = [*map(int, input().split())]

cap = 98
prev = 2
crt = l[0]

for i in range(1, n):
    if crt == l[i]:
        prev *= 2
    else:
        prev = 2
        crt = l[i]
    cap -= prev

    if cap <= 0:
        crt = -1
        cap = 100
print(100 - cap)