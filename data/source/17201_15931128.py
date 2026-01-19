n=input()
a=list(input())
for i in range(1,len(a)//2):
    if a[(i-1) * 2 + 1 ]== a[i*2]:
        print("No")
        break
else:
    print("Yes")