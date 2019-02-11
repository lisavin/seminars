n = int(input())
graf = []
while n > 0:
    line = list(map(int, input().split()))
    graf.append(line)
    n -= 1
print (graf)
for lin in graf:
    for elem in lin:
        if elem 