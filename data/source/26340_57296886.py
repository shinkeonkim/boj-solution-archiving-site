for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x, y, z = a, b, c
    
    for __ in range(c):
        if a > b:
            a //= 2
        else:
            b //= 2
    print("Data set:", x, y, z)
    print(max(a, b), min(a, b))
    print()