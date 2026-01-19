n = int(input())
l = [*map(int,input().split())]
s = sum(l) + (n-1)*8

print(s//24,s%24)
