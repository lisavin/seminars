def smile(a):
    k = 0
    state = 0
    c = 0
    for c in a:
        if state == 0:
            if c in {";", ":"}:
                state = 1
        elif state == 1:
            if c == "-" or c in {";", ":"}:
                pass
            elif c in {"(", ")", "[", "]"}:
                k += 1
                state = 0
            else:
                state = 0
        return k


s = input()
print(smile(s))