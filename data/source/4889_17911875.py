case = 1
while True:
    cnt = 0
    cnt0 = 0
    ans = 0
    s = input()
    if s[0]=="-":
        break
    for i in s:
        if i == '{':
            cnt+=1
        else:
            if cnt <= 0:
                ans+=1
                cnt+=1
            else:
                cnt-=1
    ans += cnt//2

    print("{}. {}".format(case,ans))

    case +=1