n = int(input()) - 1
a = chr(97 + n % 8)
b = str(n // 8 + 1)
print(a+b)
