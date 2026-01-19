for tc in range(1, int(input()) + 1):
  h, m = map(int, input().split())
  
  t = ((h * 60 + m - 45) + 1440) % 1440
  
  print(f"Case #{tc}: {t // 60} {t % 60}")