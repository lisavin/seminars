i=1
while i<10:
    if i%8 == 0:
        print ("{0} here is 8".format (i))
        break
    if i%2 == 0:
        print ("{0} - even".format (i))
        i+=1
        continue
        print ("insert 1")
    elif i%2 == 1:
        print ("{0} - odd".format (i))
        i+=1
        continue
        print("insert 1")
    print("insert 3")
else:
    print("in else!")