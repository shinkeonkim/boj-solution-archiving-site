n = int(input())
l = sorted(list(set([*map(int, input().split())])))

if min(l) != 1 or max(l) != n or len(l) != n:
    print("NIE")
else:
    print("TAK")