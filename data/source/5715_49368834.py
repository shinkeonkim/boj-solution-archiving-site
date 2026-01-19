note_duration = {
  'X': 1,
  'T': 2,
  'S': 4,
  'E': 8,
  'Q': 16,
  'H': 32,
  'W': 64,
}

while 1:
  s = input()
  ans = 0

  if s == "*":
    break

  durations = s.split("/")

  for duration in durations:
    num = 0
    for note in duration:
      num += note_duration[note]
    if num == 64:
      ans += 1

  print(ans)
