# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите число ', ))
n_list = []
numbers = 0
degree = 0
while numbers < number:
    numbers = 2**degree
    degree +=1
    if numbers<number:
        n_list.append(numbers)
print(n_list)
