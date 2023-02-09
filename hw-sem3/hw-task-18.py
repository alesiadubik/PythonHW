# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input('Введите кол-во элементов: ', ))
start_list = []
for i in range(n):
    element = int(input('элемент: '))
    start_list.append(element)
print(start_list)
x = int(input('Введите число: ', ))
temp = start_list[0]
result = 0
for i in range(len(start_list)-1):
    if (abs(x-start_list[i]))<(abs(x-start_list[i+1])):
        result = start_list[i]
    else:
        result = start_list[i+1]
    if (abs(x-temp))>(abs(x-result)):
        temp = result
print(f'-> ',temp)