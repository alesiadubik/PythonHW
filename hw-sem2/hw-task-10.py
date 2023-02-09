# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Number icons: ', ))
icons_list = []
for i in range(n):
    icon = int(input('icon: '))
    icons_list.append(icon)
print(icons_list)
orel_0 = 0
reshka_1 = 0
for i in range(len(icons_list)):
    if icons_list[i] == 0:
        orel_0 += 1
    else:
        reshka_1 +=1
print(orel_0 if orel_0 < reshka_1 else reshka_1)
