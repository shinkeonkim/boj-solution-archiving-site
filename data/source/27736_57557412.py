N = int(input())
l = [*map(int, input().split())]

zero = l.count(0)
one = l.count(1)
minus = l.count(-1)

if zero * 2 >= N:
    print("INVALID")
elif one <= minus:
    print("REJECTED")
else:
    print("APPROVED")