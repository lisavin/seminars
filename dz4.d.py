n = int(input())
mn = int('1'+'0'*(n-1))
mx = int('9'*n)
for i in range(mx, mn, -2):
    print(i, end=' ')
if n==1:
    print(1)