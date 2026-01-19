n=input()
print("no" if sum(list(map(int,input().split()))) % 3  else "yes")