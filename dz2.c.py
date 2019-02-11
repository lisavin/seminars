a=int(input())
b=1
while b<=a+1:
    for i in range(1, b):
        print('{0}'.format(i), end='')
    if (b!=1): print ('')
    b+=1