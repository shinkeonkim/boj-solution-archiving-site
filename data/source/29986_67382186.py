n, h = map(int, input().split())
print(sum([int(h >= i) for i in [*map(int, input().split())]]))