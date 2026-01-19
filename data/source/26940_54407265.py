n = int(input())
l = [*map(int, input().split())]

print(sum([l[i] > l[i-1] for i in range(1, n)]))

