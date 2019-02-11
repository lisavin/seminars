length = int(input())
A = list(map(int, input().split()))
key = int(input())
A = A[0:length]
def search (A, key):
    count = 0
    for i in range (len(A)):
            if A[i] == key:
                count += 1
    return count
print (search (A, key))