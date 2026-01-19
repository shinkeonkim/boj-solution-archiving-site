n = int(input())
l = [*map(int, input().split())]

i = l.index(max(l))

print(sum(l[:i]), sum(l[i+1:]),sep="\n")