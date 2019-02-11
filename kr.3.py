r=int(input())
s=list(map(int, input().split()))
s.sort()
#s.reverse()
#print (s)
n=0
for i in range (len(s)):
    if s[i]>=r:
        n=1
for i in range (len(s)-1):
    if s[i+1]-s[i]>=3:
        n+=1
print (n)