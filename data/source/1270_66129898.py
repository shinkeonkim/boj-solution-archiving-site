for _ in range(int(input())):
    n, *l = [*map(int, input().split())]

    d = {}

    for i in l:
        try:
            d[i] += 1
        except:
            d[i] = 1

    for i, j in d.items():
        if j * 2 > n:
            print(i)
            break
    else:
        print("SYJKGW")