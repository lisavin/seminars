str=input()
if str.find('f')==-1: print('-2')
if str.find('f')!=-1:
    a=str.find('f')
    s=str[a+1:len(str)+1]
    if s.find('f')!=-1:
        print (s.find('f')+a+1)
    else: print('-1')