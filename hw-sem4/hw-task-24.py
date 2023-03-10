# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

n_bushes = int (input('Введите кол-во кустов:\n'))
set_berries = [int (input('Введите кол-во ягод на каждом кусте:\n')) for i in range(n_bushes)]
max_sum = 0
for i in set_berries:
    summ = sum(set_berries[i:i+3])
    if summ > max_sum:
        max_sum = summ
if set_berries[0] + set_berries[1] + set_berries[-1] > max_sum:
  max_sum = set_berries[0] + set_berries[1] + set_berries[-1]
if set_berries[0] + set_berries[-1] + set_berries[-2] > max_sum:
  max_sum = set_berries[0] + set_berries[-1] + set_berries[-2]

print(max_sum)
