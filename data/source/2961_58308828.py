n = int(input())
l = [[*map(int, input().split())] for i in range(n)]
chk = [0] * n
ans = 10000000000000000
def g():
    global n, l, chk, ans
    
    if chk.count(1) == 0:
        return

    sm = 0
    mul = 1
    
    for i in range(n):
        if chk[i]:
            sm += l[i][1]
            mul *= l[i][0]
    ans = min(ans, abs(sm - mul))
    

def f(idx):
    global n, chk
    if idx == n - 1:
        for i in range(2):
            chk[idx] = i
            g()
    else:
        for i in range(2):
            chk[idx] = i
            f(idx + 1)

f(0)
print(ans)