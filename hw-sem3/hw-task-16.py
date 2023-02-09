# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input('Введите кол-во элементов: ', ))
start_list = []
for i in range(n):
    element = int(input('элемент: '))
    start_list.append(element)
print(start_list)
x = int(input('Введите искомое число: ', ))
count = 0
for j in range(len(start_list)):
    if start_list[j] == x:
        count+=1
print(f'-->',count)

