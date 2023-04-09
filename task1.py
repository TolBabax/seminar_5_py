# Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def exponent(number_a: int, number_b: int) -> bool:
    if not isinstance(number_a, int) and not isinstance(number_b, int): return None
    
    if number_b == 0:
        return 1 
    return exponent(number_a, number_b - 1)*number_a

print(exponent(2, 0))