Year = int(input())
if Year % 400 ==0 or (Year % 4==0 and Year % 100 != 0): print(1)
else: print(0)