n, c = map(int,input().split())
a = list(set([int(input()) for i in range(n)]))
time_line = [0] * (c + 1)
for i in a:
    for j in range(i, c + 1, i):
        time_line[j]=1

print(time_line.count(1))