'''Задача №1. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120'''

num = int(input("Введите N:"))

# factorial = 1
# while num > 1:
#     factorial *= num
#     num -= 1
# print(factorial)

# for el in range(1, num +1):
#     factorial *= el5

# print(f)

def factorial(num, f = 1):
    if num == 0:
        return f
    return factorial(num - 1, f * num)
print(factorial(num))
