a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(5):
    if a[i]==b[i]:
        print("N")
        break
else:
    print("Y")