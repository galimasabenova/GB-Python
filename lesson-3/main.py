
# Задание 1
def div_func():
    try:
        arg_1 = float(input('Введите первое число:'))
        arg_2 = float(input('Введите второе число:'))
    except ValueError:
        return 'Введены не числа, повторите ввод'
    try:
        res = arg_1 / arg_2
    except ZeroDivisionError:
        return 'Деление на ноль!'
    return res

print(div_func())

print('*'*33)

# Задание 2, вариант 1

def user_(numb_client, **kwargs):
    print(numb_client, end=' ')
    for i, j in kwargs.items():
        print(f'{i} - {j};', end=' ')

user_1 = user_('Клиент № 1:', name = 'Галя', surname = 'Ссс', date_of_b = '2000', city = 'Айтаун', email = '5@mail.ru', tel = '6666-66-66')
user_2 = user_('Клиент № 2:', name = 'Лиля', fam = 'Ттт', gr = '2000', gor = 'Айтаун', em = '9@mail.ru', tel = '466-66-66')

print('*'*33)

# Задание 2, вариант 2

def user_(numb_client, name, surname, date_of_b, city, email, tel):
    print(numb_client, name, surname, date_of_b, city, email, tel)


user_('Клиент №1', name='Igor', surname='Danilov', date_of_b='2002', city='Toronto', email='d@mail.ru', tel='333-33-33')

print('*'*33)

# Задание 3

def my_func(arg_1, arg_2, arg_3):
    list_=[arg_1, arg_2, arg_3]
    res1 = max(list_)
    list_.remove(res1)
    res2 = max(list_)
    return res1 + res2

sum_ = my_func(1, 2, 3)
print(sum_)

print('*'*33)

# Задание 4, вариант 1

def my_func(x, y):
    return x ** y

res = my_func(2.3, -5)
print(res)

print('*'*33)

# Задание 4, вариант 2

def my_func_2(x, y):
    res = 1
    for i in range(abs(y)):
        res = res*x
    if y < 0:
        return 1/res
    else:
        return res

print(my_func_2(2.3, -5))

print('*'*33)

# Задание 5

def st_ch():
    st2 = 0
    while True:
        try:
            st = input('введите числа чз пробел:').split(' ')
            st1 = list(map(float, st))
            st2 = st2 + sum(st1)
            print(st2)
        except ValueError:
            for i in range(len(st)):
                try:
                    st2 = st2 + i
                except ValueError:
                    break
            return st2

print(st_ch())

print('*'*33)

# Задание 6

def int_func(txt):
    s = txt.capitalize()
    return s

res = int_func('qqq qqq qqq')
print(res)

print('*'*33)

# Задание 7

def int_func_2():
    s = input('введите слова через пробел:').title()
    return s

print(int_func_2())

print('*'*33)