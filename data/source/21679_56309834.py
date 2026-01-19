input()
mx = [*map(int, input().split())]
input()
for i in [*map(int, input().split())]:
  mx[i - 1] -= 1
for i in mx:
  print("yes" if i < 0 else "no")
