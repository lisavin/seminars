def dlina(a, b, c, d):
    x=(c-a)*(c-a)+(d-b)*(d-b)
    return (x**0.5)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print (dlina(a, b, c, d))
