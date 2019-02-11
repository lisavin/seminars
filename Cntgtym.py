def stepen(a, n):
    if n == 0:
        return 1
    else:
        return a * stepen(a, n - 1)


def stepen1(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return stepen1(a * a, n/2)
    else:
        return a * stepen1(a, n - 1)


e = float(input())
d = int(input())
if d % 2 == 0:
    print(stepen1(e,d))
else:
    print(stepen1(e, d))