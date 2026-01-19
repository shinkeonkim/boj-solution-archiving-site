for tc in range(1, int(input()) + 1):
  n = int(input())
  if n <= 25:
    print(f"Case #{tc}: World Finals")
  elif n <= 1000:
    print(f"Case #{tc}: Round 3")
  elif n <= 4500:
    print(f"Case #{tc}: Round 2")
  else:
    print(f"Case #{tc}: Round 1")