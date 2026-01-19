for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a * b == c * d:
        print("Tie")
        continue
    print("Eurecom" if a * b < c * d else "TelecomParisTech")
        