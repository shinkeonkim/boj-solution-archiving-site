def get_grade(height, weight):
  if height < 140.1:
    return 6

  if height < 146:
    return 5

  if height < 159:
    return 4

  weight = weight * 10000

  if height < 161:
    if weight < 16 * height * height or weight >= 35 * height * height:
      return 4
    else:
      return 3

  if height < 204:
    if weight < 16 * height * height or weight >= 35 * height * height:
      return 4
    if weight < 18.5 * height * height or weight >= 30 * height * height:
      return 3
    if weight < 20 * height * height or weight >= 25 * height * height:
      return 2
    return 1

  return 4

for i in range(int(input())):
  print(get_grade(*map(int, input().split())))
