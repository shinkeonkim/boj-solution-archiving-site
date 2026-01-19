l = sorted([*map(int, input().split())])
s = [*map(int, list(input()))]

print(l.index(s[0]) * 2 + int(s[2] < s[1]) + 1)
