input()
l = [*map(int, input().split())]
print(sum(l) - min(l) - max(l))