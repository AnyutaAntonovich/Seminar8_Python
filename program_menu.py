from art import tprint

from work_with_csv import input_data, print_data, change_data, delete_data


def interface():
    tprint('CONTACTS')
    while True:
        print('-' * 25)
        print('МЕНЮ ПРОГРАММЫ:\n'
              '\t1 - Ввод данных\n'
              '\t2 - Вывод данных\n'
              '\t3 - Редактирование данных\n'
              '\t4 - Удаление данных\n'
              '\t0 - Выход из программы')
        print('-' * 25)
        command = int(input('Ваш выбор: '))
        print('-' * 25)
        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            change_data()
        elif command == 4:
            delete_data()
        elif command == 0:
            print('Хороший выбор! ;)')
            return False
        else:
            print('\033[31m' + '\nВведите цифру из пункта меню:' + '\033[0m')
