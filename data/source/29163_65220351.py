n = int(input())
s = sum([i % 2 for i in [*map(int,input().split())]])

print("Happy" if n - s > s else "Sad")