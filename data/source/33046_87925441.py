a, b = map(int, input().split())
c, d = map(int, input().split())

s = a + b + c + d - 1

s = s % 4

if s == 0:
    s = 4
    
print(s)
