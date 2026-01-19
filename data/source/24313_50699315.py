a, b = map(int, input().split())
c = int(input())
n = int(input())

print(int((c - a) * n >= b) and int((c - a) * (n + 10000) >= b))
