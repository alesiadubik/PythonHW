# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
#min 7 max 10
# Вывод: [1, 9, 13, 14, 19]

n = int(input('Введите кол-во n элементов: ', ))
our_list = [int(input('num: ')) for i in range(n)]
print(our_list)
min_item = int(input('Введите значение min элемента: ', ))
max_item = int(input('Введите значение max элемента: ', ))
result_list = []
for i in range(len(our_list)):
    if (our_list[i]>=min_item) and (our_list[i]<=max_item):
        result_list.append(i)
print(result_list)