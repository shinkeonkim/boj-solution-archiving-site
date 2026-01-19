for i in range(int(input())):
  s = input()
  print(f'The number of vowels in {s} is {sum([s.count(c) for c in "aeiou"])}.')
