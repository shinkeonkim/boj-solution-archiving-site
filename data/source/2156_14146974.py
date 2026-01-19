def solution(ar):
    # 여기에 코드를 작성해주세요.
    answer = 0
    D = [[0]*3 for i in range(len(ar))]
    D[0][1]=ar[0]
    if len(ar) >1:
        D[1][1]=ar[1]
        D[1][2]=ar[0]+ar[1]
    if len(ar) >2:
        D[2][1] = ar[0]+ar[2]
        D[2][2] = ar[1]+ar[2]
    for i in range(3,len(ar)):
        D[i][1] = max(D[i-2][2],D[i-2][1],D[i-3][1],D[i-3][2]) +ar[i]
        D[i][2] = ar[i]+D[i-1][1]
    M = 0
    for i in range(len(ar)):
        M = max(M,D[i][1],D[i][2])
    return M

L =[]
for i in range(int(input())):
    L.append(int(input()))
print(solution(L))