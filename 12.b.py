a = list(map(int, input().split()))
for i in range(1,len(a)-1):
    if a[i]%2==0:
        print(a[i], end=' ')