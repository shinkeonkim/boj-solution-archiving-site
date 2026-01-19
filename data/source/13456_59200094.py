for i in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    print(sum([a[i] != b[i] for i in range(n)]))