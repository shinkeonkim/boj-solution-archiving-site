"""
[21955: Split](https://www.acmicpc.net/problem/21955)

Tier: ??
Category: 구현
"""


def solution():
  s = input()
  n = len(s) // 2
  print(s[:n], s[n:])


if __name__ == '__main__':
  solution()
