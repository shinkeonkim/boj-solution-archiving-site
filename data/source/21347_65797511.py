a = input()
b = input()

i = 0
j = 0
ans = set()

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        ans.add(b[j])
        j += 1

while j < len(b):
    ans.add(b[j])
    j += 1

print(*ans,sep="")