str=input()
a=str.find('h')
b=str.rfind('h')
s=str[0:a+1]
t=str[a+1:b]
t1=str[a+1:b+1]
r=str[b+1:len(str)]
print(s+t+t1+r)