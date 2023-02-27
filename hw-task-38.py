# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
# 1.Вывод всех контактов
# 2.Поиск всех контактов
# 3.Добавить контакт(сразу сохранять в файл)
# 4.Выход по требованию полбзователя

import os
def all_contacts():
    with open ('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)
#all_contacts()

def find_contact(name):
    with open ('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)    
# break позволяет вывести первое попавшееся значение

def add_contact(new_contact):
    with open ('phone_number.txt', 'a', encoding='utf8') as data:
        data.write('\n'+new_contact)
        print('Контакт создан')

def edit_contact():
    with open ('phone_number.txt', 'r+', encoding='utf8') as data:
        old_name = input('Введите контакт для редактирования: ')
        new_name = input('Введите изменения: ')
        lines = data.read()
        new_lines = lines.replace(old_name, new_name)
    with open ('phone_number.txt', 'w', encoding='utf8') as data:       
        data.write(new_lines)
        print('Контакт изменён') 

def delete_contact(contact):
    with open ('phone_number.txt', 'r', encoding='utf8') as data:
        lines = data.readlines()
        with open ('phone_number.txt', 'w', encoding='utf8') as data:
            for line in lines:
                if contact in line:
                    print('Контакт удален') 
                else:
                    print(line)
                    data.write(line)  

def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомый контакт: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
    elif numb == 4:
        edit_contact()
    elif numb == 5:
        contact = input('Введите контакт для удаления: ')
        delete_contact(contact)

while True:
    numb = int(input('Введите 1 - вывод всего справочника;' 
                     '2 - поиск контакта,' 
                     '3 - создание нового контакта,'
                     '4 - редактировать контакт,'
                     '5 - удалить контакт,' 
                     '6 - выход из справочника:  ' ))
    if numb == 6:
        break
    main_menu(numb)