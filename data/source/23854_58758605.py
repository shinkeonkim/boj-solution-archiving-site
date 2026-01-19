a = int(input())
b = int(input())

if abs(a - b) % 3 != 0:
    print(-1)
else:
    if a == b:
        print(a // 3, a % 3, a // 3)
    elif a > b:
        print((a - b) // 3 + b // 3, b % 3, b // 3)
    else:
        print(a // 3, a % 3, (b - a) // 3 + a // 3)