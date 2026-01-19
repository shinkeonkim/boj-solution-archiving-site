n = int(input())
s = [input() for i in range(n)]
a = [input() for i in range(n)]

print(sum([s[i] == a[i] for i in range(n)]))