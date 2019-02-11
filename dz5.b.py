A = list(map(int, input().split()))

if len(A) == 3:
    for i in A:
        print (i, end = ' ')

else:
    max1 = A[0]
    min1 = A[0]
    for i in A:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i
    A.remove(max1)
    A.remove(min1)
    max2 = A[0]
    min2 = A[0]

    for j in A:
        if j > max2:
            max2 = j
        if j < min2:
            min2 = j
    A.remove(max2)
    max3 = A[0]

    for k in A:
        if k > max3:
            max3 = k

    otvet_min = min1 * min2 * max1
    otvet_max = max1 * max2 * max3

    if otvet_min > otvet_max:
        print(min1, min2, max1)
    else:
        print(max1, max2, max3)