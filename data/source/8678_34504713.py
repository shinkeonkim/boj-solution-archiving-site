import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().strip().split())
    print("NIE" if b % a else "TAK")