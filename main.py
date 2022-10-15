
# Задание 1

print('***** Задание 1 *****')

var_1 = 10
var_2 = 20
var_3 = 30
str_1 = 'summer'
str_2 = 'winter'
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
print(var_1 + var_2 + var_3)
print(str_1 + ' ' + str_2)
print(l_1, l_2)
print(l_1 + l_2)
name = input('Введите ваше имя:')
print(name)
age_1 = int(input('Введите ваш возраст по окончании школы:'))
age_2 = int(input('Введите ваш возраст по окончании университета:'))
print(f'Вы проучились в университете {age_2 - age_1} лет')

print('*' * 21)

# Задание 2

print('***** Задание 2 *****')

time_s = int(input('Введите время в секундах:'))
hh = time_s // 3600
mm = (time_s % 3600) // 60
ss = (time_s % 3600) % 60
print('%2d:%2d:%2d' % (hh, mm, ss))

print('*' * 21)

# Задание 3

print('***** Задание 3 *****')

n = input('Введите число n:')
nn = n + n
nnn = n + n + n
print('n + nn + nnn =', int(n) + int(nn) + int(nnn))

print('*' * 21)

# Задание 4

print('***** Задание 4 *****')

numb = int(input('Введите целое положительное число:'))
max = 0
while numb != 0:
    b = numb % 10
    if b > max:
        max = b
    numb = numb // 10
print(max)

print('*' * 21)

# Задание 5

print('***** Задание 5 *****')

reven = int(input('Введите выручку фирмы:'))
costs = int(input('Введите издержки фирмы:'))
if reven > costs:
    print('Фирма в прибыли')
    profitab = (reven - costs) / reven
    employ = int(input('Введите число сотрудников:'))
    print((reven - costs) / employ, 'прибыль на одного сотрудника')

else:
    print('Фирма в убытке')

print('*' * 21)

# Задание 6

print('***** Задание 6 *****')

a = int(input('Результат первого дня в км:'))
b = int(input('Результат последнего дня в км:'))
k = 1
while a <= b:
    a = a + a*0.1
    k = k + 1
print('Спортсмену понадобилось', k, 'дней.')

print('*' * 21)


