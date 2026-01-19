def is_and(w1, w2, B):
    for i in range(2):
        for j in range(2):
            expected = bool(i and j)
            
            res = w1 * i + w2 * j + B >= 0
            
            if expected != res:
                return "false"
    return "true"

def is_or(w1, w2, B):
    for i in range(2):
        for j in range(2):
            expected = bool(i or j)
            
            res = w1 * i + w2 * j + B >= 0
            
            if expected != res:
                return "false"
    return "true"

for _ in range(int(input())):
    s,a,b,c = input().split()
    
    if s == "AND":
        print(is_and(float(a), float(b), float(c)))
    else:
        print(is_or(float(a), float(b), float(c)))