second = int(input('Введите число: '))

sec = second%60
minute = (second//60)%60
hours = (second//6300)%24
day = (second//84600)

print(day, 'дней', hours, 'часов', minute, 'минут', sec, 'секунд')