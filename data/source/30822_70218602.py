import sys
input = sys.stdin.readline

input()
s = input()
print(min([s.count(i) for i in "uospc"]))