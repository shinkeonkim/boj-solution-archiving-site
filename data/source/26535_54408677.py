n = int(input())

a = int(n ** (1 / 2))

a = a if a * a == n else a + 1

print("x" * (a + 2))
print(("x" + "." * a + "x\n") * a, end="")
print("x" * (a + 2))
