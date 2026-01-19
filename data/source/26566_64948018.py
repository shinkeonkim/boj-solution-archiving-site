for i in range(int(input())):
    a,b=map(int,input().split())
    r, d=map(int,input().split())
    
    
    s = r*r*3.141592
    
    if a / b > s / d:
        print("Slice of pizza")
    else:
        print("Whole pizza")
    