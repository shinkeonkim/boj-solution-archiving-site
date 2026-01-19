import sys

inp = lambda : sys.stdin.readline().rstrip()
ii = lambda : int(inp())
prt = print


def solve():
  title, time = inp().split(",")

  time = int(time)

  MIN = 1
  HOUR = MIN * 60
  DAY = HOUR * 24
  YEAR = DAY * 365

  ret = []

  if time >= YEAR:
    ret.append(f"{time // YEAR} year(s)")
    time %= YEAR
  
  if time >= DAY:
    ret.append(f"{time // DAY} day(s)")
    time %= DAY
  
  if time >= HOUR:
    ret.append(f"{time // HOUR} hour(s)")
    time %= HOUR
  
  if time >= MIN:
    ret.append(f"{time // MIN} minute(s)")
    time %= MIN
  
  prt(f"{title} -", *ret)


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()