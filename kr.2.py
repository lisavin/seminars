s=[int(s)for s in input().split()]
boy=int(input())
num=0
for i in range(0,len(s)-1):
    if s[i]>=boy>s[i+1]:
        num=i+1
    if boy<=s[len(s)-1]:
        num=len(s)
print(num+1)