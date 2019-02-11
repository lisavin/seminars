s=list(map(int, input().split()))
k=0
for i in range (len(s)):
    if s[i]>0:
        k+=1
print (k)