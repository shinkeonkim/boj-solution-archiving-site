s = input()

for i in s:
  t = ord(i)
  
  if 97 <= t <= 122:
    t -= 96
    print(f"{t:02d}", end="")
  elif 65 <= t <= 90:
    t -= 38
    print(f"{t:02d}", end="")
  elif 48 <= t <= 57:
    print(f"#{i}", end="")
  else:
    print(end=i)

    