a=b=c=d=0
while True:
    try:
        L = sorted(list(map(int,input().split())))

        if L[0] + L[1] <= L[2]:
            break
        a+=1
        if L[2]*L[2] == L[0] * L[0] + L[1]*L[1]:
            b+=1
        if L[2]*L[2] < L[0] * L[0] + L[1]*L[1]:
            c+=1
        if L[2]*L[2] > L[0] * L[0] + L[1]*L[1]:
            d+=1
    except:
        break
print(a,b,c,d)