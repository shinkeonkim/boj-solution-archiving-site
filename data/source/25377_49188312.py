INF = 999999999999

def solution(l):
  ans = INF

  for a, b in l:
    if a <= b:
      ans = min(b, ans)

  return -1 if ans == INF else ans


if __name__ == "__main__":
  print(solution([[*map(int, input().split())] for _ in range(int(input()))]))