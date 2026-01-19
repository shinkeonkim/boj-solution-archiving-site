while 1:
    n = int(input())
    
    if n == 0:
        break
    
    l = [*map(int, input().split())]
    ans = 0

    for i in range(3, n+1):
        if l[i-4:i] == [2, 0, 2, 0]:
            ans += 1
    print(ans)