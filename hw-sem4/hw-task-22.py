# Задача 22-1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите кол-во n элементов: ', ))
n_set=set([int (input('Элемент:\n')) for i in range(n)])
print(n_set)
m = int(input('Введите кол-во m элементов: ', ))
m_set = set([int (input('Элемент:\n')) for i in range(m)])
print(m_set)
union_list=list(n_set|m_set)
for i in range(len(union_list)):
    for j in range(i + 1, len(union_list)):
        if union_list[i] > union_list[j]:
           union_list[i], union_list[j] = union_list[j], union_list[i]
print(f'---->', union_list)
