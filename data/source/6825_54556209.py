w = float(input())
h = float(input())

k = h * h

if w < 18.5 * k:
    print("Underweight")
elif w <= 25 * k:
    print("Normal weight")
else:
    print("Overweight")
