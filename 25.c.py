m = list(map(int, input().split()))
n = list(map(int, input().split()))

a = m[0]
b = m[1]
c = n[0]
d = n[1]

otvet = []

for i in range (10000, 99999):
    if i % a == b and i % c == d:
        otvet.append(i)

for i in otvet:
    print(i, end = " ")

