n = int(input())
print(sum([1 if 1 <= i <= n else 0 for i in list(set([int(input()) for i in range(n)]))]))
