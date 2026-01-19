for i in range(3):
    a = input()
    c = 1
    Max = 1
    for j in range(1,len(a)):
        if a[j] == a[j-1]:
            c +=1
        else:
            c = 1
        Max = max(Max,c)
    print(Max)