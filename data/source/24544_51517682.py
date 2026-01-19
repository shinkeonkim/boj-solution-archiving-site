n = int(input())
score = [*map(int, input().split())]
check = [*map(int, input().split())]

print(sum(score))
print(sum([0 if check[i] else score[i] for i in range(n)]))
