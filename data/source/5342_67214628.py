d = {
    "Paper": 5799,
    "Printer": 12050,
    "Planners": 3125,
    "Binders": 2250,
    "Calendar": 1095,
    "Notebooks": 1120,
    "Ink": 6695,
}

ans = 0
while 1:
    s = input()
    if s == "EOI":
        break

    ans += d[s]
print("$%.2f" % (ans / 100))