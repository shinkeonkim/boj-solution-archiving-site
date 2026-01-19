a = sorted([*map(int, input().split())])
b = sorted([*map(int, input().split())])

print(sum([a[i] * b[i] for i in range(3)]))