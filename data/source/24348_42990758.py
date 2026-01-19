l=sorted([*map(int,input().split())])
print(max(l[2]*l[1]+l[0], l[2]+l[1]*l[0]))
