n, k = input().split()
print(len(set(input() for i in range(int(n)))) // {'Y' : 1, 'F': 2, 'O': 3}[k])
