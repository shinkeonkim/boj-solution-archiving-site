n, fixed = map(int, input().split())
salaries = [int(input()) for i in range(n)]

a = sum([salary < fixed for salary in salaries])
same = salaries.count(fixed)
b = n - a - same

print(1 if a > b else (2 if a < b else 0))
