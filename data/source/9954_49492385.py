sentences = []

while 1:
  a = input()

  if a == '#':
    break

  sentences.append(a)


for sentence in sentences:
  key = sentence[-1]
  count = ord(key) - ord('A')

  for char in sentence[:-1]:
    if 'a' <= char <= 'z':
      print(end=chr((ord(char) - 97 - count + 26) % 26 + 97))
    elif 'A' <= char <= 'Z':
      print(end=chr((ord(char) - 65 - count + 26) % 26 + 65))
    else:
      print(end=char)

  print()
