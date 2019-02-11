def Ispointinsquare(x,y):
    while x<=1 and x>=-1 and y<=1 and y>=-1:
        return (True)
    else: return (False)

x=float(input())
y=float(input())
if Ispointinsquare(x,y)==True:
    print('YES')
else: print('NO')
