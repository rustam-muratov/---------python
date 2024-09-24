'''Задача №65. Решение в группах
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
'''

from seaborn import load_dataset, scatterplot

penguins = load_dataset('penguins')


def f_1():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    sohw()

f_1()
    