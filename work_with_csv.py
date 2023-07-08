import csv

from data_input import input_user_data


def input_data():
    name, surname, phone, address = input_user_data()
    with open('phone_book.csv', 'a', encoding='utf-8') as file:
        file.write(f'{name};{surname};{phone};{address}\n')
    print(f'\033[32mДанные успешно записаны!\033[0m')


def change_data():
    print('Содержимое телефонной книги:'
          'NAME;SURNAME;PHONE;ADDRESS')
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    for key, line in enumerate(lines):
        print(f'{key}: {line}')
    str_to_change = int(input('Введите номер строки, в которой нужно изменить данные: '))
    temp_str = lines[str_to_change].split(';')
    print('Замените старые данные на новые..')
    temp_str[0], temp_str[1], temp_str[2], temp_str[3] = input_user_data()
    lines[str_to_change] = ';'.join(temp_str)

    with open('phone_book.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print(f'\033[32mДанные успешно записаны!\033[0m')


def delete_data():
    print('Содержимое телефонной книги:\n'
          'NAME;SURNAME;PHONE;ADDRESS')
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    for key, line in enumerate(lines):
        print(f'{key}: {line}')
    str_to_delete = int(input('Введите номер строки, которую нужно удалить: '))
    del lines[str_to_delete]
    with open('phone_book.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print(f'\033[32mДанные успешно записаны!\033[0m')


def print_data():
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        print('Содержимое телефонной книги:\n'
              'NAME;SURNAME;PHONE;ADDRESS')
        print(''.join(file.readlines()))
