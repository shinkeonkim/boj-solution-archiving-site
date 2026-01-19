n = int(input())
statuses = [*map(int, input().split())]

for i in range(int(input())):
    s, num = map(int, input().split())
    
    if s == 1:  # boy
        for j in range(num, n+1, num):
            statuses[j - 1] = 1 - statuses[j - 1]
    else:  # girl
        num -= 1
        statuses[num] = 1 - statuses[num]
        for j in range(1, n):
            if num + j >= n or num - j < 0:
                break
            if statuses[num + j] != statuses[num - j]:
                break
            
            statuses[num + j] = 1 - statuses[num + j]
            statuses[num - j] = 1 - statuses[num - j]

for i in range(0, n, 20):
    print(*statuses[i:i+20])
