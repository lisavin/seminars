n = int(input())        #загадано от 1 до n
is_possible = [0] * n  #массив возможных
line = input()         #считываем ее предположение
while line != "HELP":  #пока она не сдается
    answer = input()   #считываем его ответ
    numbers = list(map(int, line.split()))   #преобразуем ее ответ, чтобы было удобно работать
    line = input()     #считываем ее новое предположение
    for i in numbers:  #для элементов в ее ответе
        if answer == "YES":  #если в ее ответе было число загаданное
            is_possible[i - 1] += 1   #ко всем числам, которые были в запросе прибавляем единицу
        if answer == "NO":   #если не угадала
            is_possible[i - 1] -= 1   #то из запроса вычитаем единицу
s = ""                                #дальше выводим те, у которых счет максимален
max = 0
for i in range(n):
    if is_possible[i - 1] > max:
        max = is_possible[i - 1]
for i in range(n):
    if is_possible[i - 1] == max:
        s += str(i) + " "
print(s)