def solution():
  a = input()
  b = input()

  a, b = len(b) * a, len(a) * b

  return 1 if a == b else 0


if __name__ == '__main__':
  print(solution())