X = input()
cnt = 0
while(len(X) > 1):
    cnt+=1
    X = str(sum(list(map(int,list(X)))))
print(cnt)
print("YES" if int(X)%3 ==0 else "NO")