a = int(input())
while a % 10 == 0:
    a //= 10
print(str(a).count('0'))