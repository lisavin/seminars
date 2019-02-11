A = list(map(int, input().split()))
def BubbleSort(A):
    j = len(A) - 1
    IsNotOrdered = True
    while IsNotOrdered:
        IsNotOrdered = False
        for i in range(0, j):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                IsNotOrdered = True
        j -= 1
    return A
otvet = BubbleSort(A)
for i in otvet:
    print(i, end = ' ')