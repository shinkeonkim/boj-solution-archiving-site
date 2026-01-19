for i in range(int(input())):
    x, y = map(float, input().split())
    print("golden" if abs((2 * x / y - 1) ** 2 - 5) <= 0.01 else "not")