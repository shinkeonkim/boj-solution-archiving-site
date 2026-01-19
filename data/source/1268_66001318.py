n = int(input())

ans = 1
mx = 0

l = [[*map(int, input().split())] for i in range(n)]

for i in range(n):    
    s = set()
    for j in range(n):
        if i == j:
            continue
        

        for k in range(5):
            if l[i][k] == l[j][k]:
                s.add(j)

    if len(s) > mx:
        mx = len(s)
        ans = i + 1
print(ans)