N = int(input())
L = []
while True:
    try:
        L.extend(list(input().split()))
    except:
        break

numbers = []
for s in range(N):
    for e in range(s+1, N+1):
        numbers.append(int("".join(L[s:e])))
numbers = list(set(numbers))
numbers.sort()

mn = -1
for i in numbers:
    if i == mn + 1:
        mn+=1
    elif i > mn + 1:
        print(mn + 1)
        break
