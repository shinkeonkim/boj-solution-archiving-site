N, M = map(int,input().split())
numbers = [int(input()) for _ in range(N)]

for card in range(1, M+1):
    for student in range(0, N-1):
        if numbers[student] % card > numbers[student + 1] % card:
            numbers[student],numbers[student + 1] = numbers[student + 1],numbers[student]
for i in numbers:
    print(i)