n = int(input())
l = [*map(int, input().split())]

a = b = 0

for i in range(1, n):
	if l[i - 1] < l[i]:
		b += l[i] - l[i - 1]
	else:
		a += l[i - 1] - l[i]
print(a, b)