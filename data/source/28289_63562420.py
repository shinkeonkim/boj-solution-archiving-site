n = int(input())
l = [[*map(int, input().split())] for i in range(n)]


print(sum([i[1] <= 2 and i[0] != 1 for i in l]))
print(sum([i[1] == 3 and i[0] != 1 for i in l]))
print(sum([i[1] == 4 and i[0] != 1 for i in l]))
print(sum([i[0] == 1 for i in l]))