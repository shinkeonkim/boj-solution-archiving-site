import sys
sys.setrecursionlimit(100000000)

l = []

def dfs(idx, s, e):
    global l

    if idx == s == e:
        print(l[idx])
        return

    if s > e or s < 0 or e < 0:
        return

    r = e + 1
    for i in range(s, e + 1):
        if l[idx] < l[i]:
            r = i
            break

    # if e - s == 1:
    #     print(l[s])
    #     print(l[e])
    dfs(idx + 1, s + 1, r - 1)
    dfs(r, r, e)

    print(l[idx])

while 1:
    try:
        n = int(input())
    except:
        break
    l.append(n)

dfs(0, 0, len(l) - 1)