for i in range(int(input())):
    a, b = map(float, input().split())
    d = a * b / (a + b)
    print(f"f = {d:.1f}")