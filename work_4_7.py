print('Введите натуральное число, не превосходящее 1 000 000 000:')
num = int(input())
num_new = num % 1000
num_new1 = num_new % 10
num_new2 = (num_new % 100) // 10
num_new3 = num_new // 100
print('У числа', num_new, 'сумма последних трех цифр равна', num_new1 + num_new2 + num_new3)

