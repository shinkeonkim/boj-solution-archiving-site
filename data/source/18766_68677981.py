for _ in range(int(input())):
    input()
    a = sorted(input().split())
    b = sorted(input().split())

    if a == b:
        print("NOT CHEATER")
    else:
        print("CHEATER")