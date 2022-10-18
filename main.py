# Задание 2-1
print('Задание 2-1')
my_list = ['a', 1, 2.3, [4, 5], (6, 7), True]
print(my_list)
for i in my_list:
    print(f'"{i}" элемент типа {type(i)}')

print('*' * 21)

# Задание 2-2
print('Задание 2-2')
new_inp = input('Введите элементы списка через пробел:')
new_list = new_inp.split(' ')
i = 0
while i in range(len(new_list)-1):
    a = new_list[i]
    new_list[i] = new_list[i+1]
    new_list[i+1] = a
    i = i + 2
print(new_list)

print('*' * 21)

# Задание 2-3
print('Задание 2-3')
month = int(input('Введите номер месяца от 1 до 12:'))
if month not in range(1, 13):
    print('Вы ввели не номер месяца')
m_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for s, m in m_dict.items():
    if month in m:
        print(s)

print('*' * 21)

# Задание 2-4
print('Задание 2-4')
s_str = input('Введите слова через пробел:')
s_list = s_str.split(' ')

for ind, el in enumerate(s_list, 1):
    print(ind, '%.10s' % (el))

print('*' * 21)

# Задание 2-5
print('Задание 2-5')
my_list = [7, 5, 3, 3, 2]
print(my_list)
print('Введите целое число для добавления в список по рангу:')
num = int(input())
i = 0
for i in range(len(my_list)): # i 0-5
    if num > my_list[i]:
        my_list.insert(i, num)
        break
    elif num <= my_list[len(my_list)-1]:
        my_list.append(num)
        break
    elif num == my_list[i] and num != my_list[i+1]:
        my_list.insert(i+1, num)
        break
print(my_list)

print('*' * 21)

# Задание 2-6
print('Задание 2-6')
list_1 = (input('Товар №1 (введите название, цену, кол-во, ед. изм. через пробел):')).split(' ')
list_2 = (input('Товар №2 (введите название, цену, кол-во, ед. изм. через пробел):')).split(' ')
list_3 = (input('Товар №3 (введите название, цену, кол-во, ед. изм. через пробел):')).split(' ')
list_ = [list_1, list_2, list_3]
n_l = zip(*list_)
tr_list_ = list(n_l)
tovary = [(), (), ()]
for i in range(3):
    tovary[i] = (
    i + 1, {'название': list_[i][0], 'цена': list_[i][1], 'количество': list_[i][2], 'ед.изм.': list_[i][3]})
# print(tovary)
n_dict = {}
n_keys = list(tovary[0][1].keys())
for i in range(4):
    n_dict[n_keys[i]] = list(tr_list_[i])

print('Список товаров: ', tovary)
print('Каталог по характеристикам: ', n_dict)

print('*' * 21)
