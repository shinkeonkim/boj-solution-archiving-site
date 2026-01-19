n = int(input())

for y in range(5):
	for y2 in range(n):
		for x in range(5):
			for x2 in range(n):
				if (x % 2 == 0) or (y == 0 and x == 1) or (y == 4 and x == 3):
					print(end="@")
				else:
					print(end=" ")
		print()
