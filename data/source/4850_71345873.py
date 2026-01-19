while 1:
    try:
        n, w, d, s = map(int,input().split())
    except:
        break
    z = n * (n - 1) // 2 * w

    if s == z:
        print(n)
    else:
        print((z - s) // d)