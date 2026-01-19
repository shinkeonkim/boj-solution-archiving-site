def f(l):
  return sum([[6,3,2,1,2][i]*l[i] for i in range(5)])

print(f([*map(int,input().split())]), f([*map(int,input().split())]))
