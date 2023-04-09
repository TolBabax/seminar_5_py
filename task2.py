# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def summa(number_a, number_b):
    if number_a == 0 and number_b == 0: return 0
    if number_a !=0:
        return summa(number_a-1, number_b) + 1
    return summa(number_a, number_b-1) + 1

print(summa(3,2))