def f(a, b, c):
    return 3 * a + b * 20 + c * 120

a = f(*map(int, input().split()))
b = f(*map(int, input().split()))

print("Max" if a > b else "Mel" if a < b else "Draw")