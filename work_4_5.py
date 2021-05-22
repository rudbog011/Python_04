print('Введите целое число - количество секунд')
sec = int(input())
seconds = (sec % 60)
minutes = (sec % 3600) // 60
hour = sec // 3600
print(sec, 'секунд - это', hour, 'час', minutes, 'минут', seconds, 'сек')