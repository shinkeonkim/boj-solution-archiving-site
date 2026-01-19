print("JABCDEFGHIZ"[sum([[2, 7, 6, 5, 4, 3, 2][idx] * number for idx, number in enumerate([*map(int, [*input()])])])%11])
