def f(a):
  if a < 425:
    return "Violet"
  if a < 450:
    return "Indigo"
  if a < 495:
    return "Blue"
  if a < 570:
    return "Green"
  if a < 590:
    return "Yellow"
  if a < 620:
    return "Orange"
  return "Red"

print(f(int(input())))
