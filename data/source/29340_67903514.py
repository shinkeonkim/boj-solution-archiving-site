a = [*map(int, list(input()))]
b = [*map(int, list(input()))]

for i in range(len(a)):
    print(max(a[i],b[i]),end="")