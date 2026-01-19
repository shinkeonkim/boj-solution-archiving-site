ans = ""
l = [
  ["B", "v"],
  ["E", "ye"],
  ["H", "n"],
  ["P", "r"],
  ["C", "s"],
  ["Y", "u"],
  ["X", "h"],
]

s = input()
for a, b in l:
  s = s.replace(a, b)

print(s.lower())
