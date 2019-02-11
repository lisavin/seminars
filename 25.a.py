m = list(map(int, input().split()))#получ аем значения размеров, добавляем в список
stroka = int(m[0])   #количество строк - первое значение
stolb = int(m[1])    #количество столбцов - второе значение

a = []  #создаем пустой список, потом добавляем полученное количество строк, и внутри списка делаем еще списки = столбцы
for r in range(stroka):
    a.append([0])
    for c in range(stolb-1):
        a[r].append(0)

wow = int(m[2])

while wow > 0:
    k = list(map(int, input().split()))
    i = int(k[0])
    j = int(k[1])
    wow -= 1
    a[i-1][j-1] = '*'

c = 0
for v in range (stolb-3, stolb+3):
    for n in range (stroka-3, stroka+3):
        if a[v][n] != '*':

            if a[v - 1][n - 1] == '*':
                c += 1
            if a[v - 1][n] == '*':
                c += 1
            if a[v - 1][n + 1] == '*':
                c += 1
            if a[v][n - 1] == '*':
                c += 1
            if a[v][n + 1] == '*':
                c += 1
            if a[v + 1][n - 1] == '*':
                c += 1
            if a[v + 1][n] == '*':
                c += 1
            if a[v + 1][n + 1] == '*':
                c += 1
        a [v][n] = c





for row in a:
    print(' '.join(list(map(str, row))))
