a=input()
L=input().split()
s=set()
for i in L:
    s.add(i[0])
if len(s) == 1:
    print(1)
else:
    print(0)