l = [int(input()) for _ in range(int(input()))]

if min(l) == l[0]:
    print("ez")
elif max(l) == l[0]:
    print("hard")
else:
    print("?")
