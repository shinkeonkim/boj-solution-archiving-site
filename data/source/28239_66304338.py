for i in range(int(input())):
    a = bin(int(input()))[2:][::-1]

    ans = []
    for i in range(len(a)):
        if a[i] == '1':
            ans.append(i)
    
    if len(ans) == 1:
        print(ans[0] - 1, ans[0] - 1)
    else:
        print(*ans)
