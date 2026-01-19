from sys import stdin, exit

s = sorted(list(input()))
n = int(input())
d = {}

for i in range(n):
    w = stdin.readline()[0]
    
    try:
        d[w] += 1
    except:
        d[w] = 1
        
for i in s:
    if i not in d or d[i] == 0:
        print(0)
        exit()
        
ret = 1
for i in s:
    ret *= d[i]
    d[i] -= 1

if s[0] == s[1] == s[2]:
    ret //= 6
elif s[0] == s[1] or s[1] == s[2]:
    ret //= 2
    
print(ret)
