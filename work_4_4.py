print('Введите рубли:')
r = int(input())
print('Введите копейки:')
k = int(input())
print('Введите количество мячей:')
n = int(input())
result = (r * 100 + k) * n
r = result // 100
k = result % 100
print('За', n, 'мяча нужно заплатить',r,'рублей и', k,'копеек')
