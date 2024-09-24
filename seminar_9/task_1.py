'''Задача №57. Решение в группах
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы'''

from pandas import read_csv # pandas это библиотека доля анолитике данных

df = read_csv('california_housing_test.csv')

print(df.shape)# Сколько слов и столбцов

print(df)
print(df.dtypes)# Типизацыя
print(df.info())
print(df.describe())