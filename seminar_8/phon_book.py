'''Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''

from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    flag = False
    while not flag:
        try:


            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Слишком короткое фамилия')
            phone_name = input('Введите телефон: ')
            if len(phone_name) < 11:
                raise NameError('Слишком короткое телефон')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_name]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_name'])
        f_w.writeheader()


def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name) #список слованей
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_name': user_data[2]}
    res.append(new_obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_name'])
        f_w.writeheader()
        f_w.writerows(res)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r) # ящик со словорями

def remove_row(file_name):
    search = int(input('Введите номер строки для удоления: '))
    res = read_file(file_name)
    if search <= len(res):

        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Введен не верный номер строки')


def copy_data(file_a, file_b):
    data_to_copy = remove_row(file_a)
    standart_write(file_b, data_to_copy)

def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_name'])
        f_w.writeheader()
        f_w.writerows(res)


file_name = 'phone.csv'
def main():
    while True:
        comand = input('Введите команду: ')
        if comand == 'q':
            break
        elif comand == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif comand == 'r':
            if not exists(file_name):
              print('Файл отсутствует, создайте файл')
              continue
            print(*read_file(file_name))
        elif comand == 'd':
            if not exists(file_name):
              print('Файл отсутствует, создайте файл')
              continue
            remove_row(file_name)
        elif comand == 'copy':
            file_a = input('Введите имя файла А: ')
            file_b = input('Введите имя файла В: ')
            copy_data(file_a, file_b)

main()
