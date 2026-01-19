n = int(input())
s = input()
d = {"N": 0, "S": 0, "W": 0, "E": 0}
for i in s:
  d[i] += 1

print(min([n - cnt for cnt in d.values()]))