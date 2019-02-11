n=1
k=int(input())
m=int(input())
while m!=0:
    if m>k:
        n+=1
        max=n
    if m<k:
        max=n
        n=1
    k=m
    m=int(input())
print(max)