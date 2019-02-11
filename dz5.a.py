A = list(map(int, input().split()))
for i in range(len(A) - 1, -1, -1):
    if A[i] == max(A):
        print(A[i], i)
        break