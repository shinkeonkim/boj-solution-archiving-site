input()
s = sum([*map(int, input().split())])

print("Right" if s > 0 else "Left" if s < 0 else "Stay")