n = int(input())
s = input()

a, b, c = 0, 0, 0
for i in range(n):
    if s[i] == '(':
        a += 1
    elif s[i] == ')':
        if a > 0:
            a -= 1
        else:
            b += 1
    else:
        c += 1

d = 0
s2 = "()"

for i in range(n):
    if s[i] == 'G':
        if b > 0:
            print(end='(')
            c -= 1
            b -= 1
        elif a > 0:
            if a == c:
                print(end = ')')
                a -= 1
                c -= 1
            else:
                print(end=s2[d])
                d = 1 - d
                c -= 1
        else:
            print(end=s2[d])
            d = 1 - d
    else:
        print(end=s[i])
