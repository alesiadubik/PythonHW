# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = int(input('Введите шестизначное число билета: ' ))
if len(str(n))!=6:
    print('Ввели неверное число')
else:        
    sum1 = (n//1000)%10 + (n//1000)//100 + ((n//1000)%100)//10
    sum2 = (n%1000)%10 + (n%1000)//100 + ((n%1000)%100)//10
    print('YES' if (sum1 == sum2) else 'NO')