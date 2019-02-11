import heapq
my_heap = []
A = list(map(int, input().split()))
for i in range (len(A)):
    heapq.heappush(my_heap, A[i])
max3 = heapq.nlargest(3, my_heap)
min2 = heapq.nsmallest(2, my_heap)
otvet_max = max3[0] * max3[1] * max3[2]
otvet_min = max3[0] * min2[0] * min2[1]
if otvet_max > otvet_min:
    print(max3[0], max3[1], max3[2])
else:
    print(max3[0], min2[0], min2[1])