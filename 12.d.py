a = list(map(int, input().split()))
c=1
for i in range(1, len(a)):
    if a[i]!=a[i-1]:
        c+=1
print(c)