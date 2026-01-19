n = int(input())
m = input()

print(n)
print(m)

for i in m[::-1]:
    print(n * int(i))
print(n * int(m))