a = [*map(int, input().split())]
b = [*map(int, input().split())]
print(sum(a) + sum(b) - min(max(a), max(b)) * 2)