a = input().count("S(")
b = input().count("S(")

if a * b == 0:
    print(0)
else:
    d = a * b
    print("S("*d+"0"+")"*d)
