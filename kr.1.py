s = list(map(int, input().split()))
m = max(s)
n = min(s)
s1 = s
s2=s

for i in range(len(s)):
    if s[i] == m:
        s2[i] = n

for i in range(len(s1)):
    if s1[i] == n:
        s2[i] = m

for i in range(len(s2)):
    print (s2[i], end=" ")
