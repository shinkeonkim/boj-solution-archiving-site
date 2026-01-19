from datetime import datetime, timedelta
d = input()
f = datetime.fromisoformat(d) + timedelta(35) <= datetime.fromisoformat("2023-10-21")
print("GOOD" if f else "TOO LATE")