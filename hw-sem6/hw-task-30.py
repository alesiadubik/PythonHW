# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arif_progress(a, d, n):
    result_list = [a]
    item = a
    while n-1:
        item+=d
        n-=1
        result_list.append(item)
    return result_list

a = int(input('Введите первый элемент: ' ))
d = int(input('Введите разность: ' ))
n = int(input('Введите количество элементов: ' ))

print(arif_progress(a,d,n))
