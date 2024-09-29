'''Задача №2. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6'''

a = 5
fiba_p, fiba_n = 0, 1
position = 2
while fiba_n < a:
    fiba_p, fiba_n = fiba_n, fiba_p + fiba_n
    position += 1
if fiba_n == a:
    print(position)
else:
    print(-1)