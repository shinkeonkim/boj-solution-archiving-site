for i in range(int(input())):
    l = [*map(int, input().split())]

    a = 18 in l
    b = 17 in l

    print(*l)

    if a and b:
        print("both")
    elif a:
        print("mack")
    elif b:
        print("zack")
    else:
        print("none")
    print()