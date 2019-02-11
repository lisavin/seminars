def perimetr(a, b, c, d, e, g):
    x=(c-a)**2+(d-b)**2
    y=(e-a)**2+(g-b)**2
    z=(e-c)**2+(g-d)**2
    return (x**0.5+y**0.5+z**0.5)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
g = float(input())
print (perimetr(a, b, c, d, e, g))
