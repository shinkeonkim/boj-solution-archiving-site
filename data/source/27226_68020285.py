a = int(input())
b = int(input())
k = int(input())

for i in range(a, b+1):
    s = i * (i - 1) // 2 + 1

    for j in range(s, s + min(i, k)):
        print(j, end=" ")
    print()