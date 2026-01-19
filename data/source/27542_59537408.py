n = int(input())
l = [*map(int, input().split())]

for i in range(n - 1):
    l2 = []
    for i in range(len(l) - 1):
        l2.append(abs(l[i] - l[i + 1]))
    l = l2

print(l[0])