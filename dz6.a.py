import numpy as np
m = list(map(int, input().split()))
size = int(m[0])
rebra = int(m[1])

a = np.zeros(( size , size ), dtype=np.int)

while rebra > 0:
    k = list(map(int, input().split()))
    i = int(k[0])
    j = int(k[1])
    rebra -= 1
    a[i-1][j-1] = 1
    a[j-1][i-1] = 1

for row in a:
    print(' '.join(list(map(str, row))))
