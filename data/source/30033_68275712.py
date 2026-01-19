n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
print(sum([int(a[i] <= b[i]) for i in range(n)]))