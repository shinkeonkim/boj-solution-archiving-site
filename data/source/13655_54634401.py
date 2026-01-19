while True:
    try:
        d, Vf, Vg = map(float,input().split())
    except:
        break

    print("S" if Vf * Vf * (144 + d * d) <= 144 * Vg * Vg else "N")
