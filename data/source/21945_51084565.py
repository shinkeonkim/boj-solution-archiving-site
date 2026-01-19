"""
[21945: Palindromes](https://www.acmicpc.net/problem/21945)

Tier: ??
Category: 문자열
"""


from re import L


def solution():
  s = 0
  input()
  for i in map(int, input().split()):
    st = str(i)
    if st == st[::-1]:
      s += i
  return s


if __name__ == '__main__':
  print(solution())
