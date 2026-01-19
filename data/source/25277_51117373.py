"""
[25277: Culture shock](https://www.acmicpc.net/problem/25277)

Tier: ??
Category: 구현
"""


def solution():
  ans = 0
  input()
  l = input().split()

  for i in l:
    if i in ['he', 'she', 'him', 'her']:
      ans += 1

  return ans


if __name__ == '__main__':
  print(solution())
