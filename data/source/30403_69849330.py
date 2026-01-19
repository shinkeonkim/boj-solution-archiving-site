A = set("ROYGBIV")
B = set("roygbiv")

input()
C = set(input())

if len(A.union(B) - C) == 0:
  print("YeS")
elif len(A - C) == 0:
  print("YES")
elif len(B - C) == 0:
  print("yes")
else:
  print("NO!")

