for i in range(int(input())):
    L = list(map(int, input().split()[1:]))
    even = odd = 0
    for i in L:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    if even > odd:
        print("EVEN")
    elif odd > even:
        print("ODD")
    else:
        print("TIE")
