from sys import exit

n = int(input())
c = sorted([*map(int, input().split())], reverse=True)
chk = [False] * n


m = int(input())

weights = sorted([*map(int, input().split())], reverse=True)
w_chk = [False] * m

if max(weights) > max(c):
    print(-1)
    exit()

crt = 0
time = 0

while crt < m:
    chk = [False] * n
    c_i = 0
    w_i = 0
    
    while c_i < n and w_i < m:
        if chk[c_i]:
            c_i += 1
            continue
        if w_chk[w_i]:
            w_i += 1
            continue
        
        if c[c_i] >= weights[w_i]:
            chk[c_i] = True
            w_chk[w_i] = True
            crt += 1
            
            c_i += 1
            w_i += 1
        else:
            w_i += 1
    time += 1
    
print(time)