"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

number = int(input("Введите натуральное число: "))
count_dig = [0,0] #odd even

def func(number, count_dig):

    if number < 10:
        if number % 2 == 0:
            count_dig[1] += 1
            return count_dig
        else:
            count_dig[0] += 1
            return count_dig
    else:
        if number % 2 == 0:
            count_dig[1] += 1
            
        else:
            count_dig[0] += 1
            
        number //= 10
        func(number, count_dig)

func(number, count_dig)
print(f"Количество нечетных и четных цифр в числе равно: {count_dig}")
