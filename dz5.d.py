def InsertionSort (A):
    for i in range (1, len (A)):
        new_elem = A[i]
        j = i - 1
        while j >= 0 and A[j] > new_elem:
            A[j +1] = A[j]
            j -= 1
        A[j+1] = new_elem
    return A
A = list(map(int, input().split()))
otvet = InsertionSort(A)
for i in otvet:
    print (i, end = ' ')