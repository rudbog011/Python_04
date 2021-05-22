print('Введите одно целое четырехзначное число')
num = int(input())
num1 = num // 1000
num2 = (num % 1000) // 100
num3 = (num % 100) // 10
num4 = num % 10
print('У числа', num, 'максимальная цифра равна', max(num1, num2, num3, num4))