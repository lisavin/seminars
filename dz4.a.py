a=input()
if len(a)%2==0:
    b=a[0:(len(a)//2)]
    c=a[(len(a)//2):len(a)]
    print(c+b)
else:
    b = a[0:(len(a) // 2)+1]
    c = a[(len(a) // 2)+1:len(a)+1]
    print(c + b)