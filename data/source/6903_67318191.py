t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    print(("*"+" "*s)*2+"*")
print("*"*(3+2*s))
print((" "*(s + 1)+"*\n")*h)