import collections
n = int(input())

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

dist = [[10000] * n for i in range(n)]

turns = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

depth = 0
dist[x1][y1] = 0
while dist[x2][y2] == 10000:
    for xc in range(n):
        for yc in range(n):
            if dist[xc][yc] == depth:
                for turn in turns:
                    xn = xc + turn[0]
                    yn = yc + turn[1]

                    if (xn >= 0 and xn < n and yn >= 0 and yn < n and dist[xn][yn] > depth + 1):
                        dist[xn][yn] = depth + 1
    depth += 1

print(dist[x2][y2])
