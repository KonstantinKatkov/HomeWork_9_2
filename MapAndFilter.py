# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел

def sqr(arg):
    return arg ** 2

def is_odd(arg):
    return arg % 2

my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(sqr, filter(is_odd, my_list))
print(f'Результат решения задачи с помощью map и filter: {list(result)}')


print()
result_1 = [x ** 2 for x in my_list if x % 2]

print(f'Результат использования списковой сборки:        {result_1}')