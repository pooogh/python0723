# # const x = 10;
# # let y = 11;

# x = 'Fedya'
# print('Hello', x)

# X = 10
# print(X - 2, x)
# print(type(10))
# print(type(2.5))
# print(type(True))
# print(type('abc'))

# # name = input()
# # print('Hello,', name)
# # age = int(input()) #'12'
# # print(type(age))
# # if age > 18:
# #     print('adult')
# # elif age == 18:
# #     print('???')
# # else:
# #     print('child')
# # print('exit')

# # дано:
# # k - студентов
# # n - мандаринов
# # сколько мандаринов достанется каждому студенту, а сколько останется?

# # тернарный
# # let x = y > 2 ? 'yes' : 'no';
# y = 2
# x = 1 if y > 2 else 3
# print(x)

# # циклы
# while x < 10:
#     print('x = ', x)
#     x += 1
# print('end')

# for i in 'a', 2, True, 23:
#     print(i)

# test = [1, 2, 'asd', True, 5.8]
# for i in test:
#     print(i)

# # (let i = 0, i < 10, i += 1)
# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 1, -2):
#     print(i)

# # range(n) от 0 до n
# # range(m, n) от m до n
# # range(m, n, s) от m до n с шагом s

# # на вход подается число n, найти n!
# # 1. через while
# # 2. через for
# # n = 3 => 3! = 1 * 2 * 3

# # генератор массива
# zeros = [0, 1] * 10
# print(zeros)

# squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
# print(squares)

# n = 5
# a = 1
# d = -2
# progr = [a + d * i for i in range(n)]
# print(progr)
# # :
# #     progr.append()

# '''
# Даны целые числа N (> 2), A и B. 
# Сформировать и вывести целочисленный массив размера N, первый элемент которого равен A, 
# второй равен B, а каждый последующий элемент равен сумме всех предыдущих.
# '''
# [1, 2, 3, 6, 12, 24]
# [2, 4, 6, 12, 24]
# [3, 5, 8, 16, 32]

# n = 10
# a = 3
# b = 7

# arr = [a, b]
# arr_tail = [arr.append(sum(arr)) for i in range(n)]

# for i in range(n):
#     arr.append(sum(arr))

# # Условие
# # Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# # Условие
# # Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# # Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# import random
# rand = [random.randint(0, 10) for i in range(10)]
# print(rand)

# # словари (объекты)
# dict_1 = dict()
# dict_2 = {} # неоч
# # [2, 2, 2] -> set() -> {2}
# dict_3 = {
#     'k1': 'v1',
#     'k2': 'v2'
# }
# dict_4 = dict([('k1', 'v1'), ('k2', 'v2')])
# dict_5 = dict(zip(['k1', 'k2', 'k3'], ['v1', 'v2', 'v3']))

# dict_5['k1'] # -> 'v1'

# try:
#     print(dict_5['k33'])
# except: # аналог  catch(e)
#     print('sorry')

# dict_5.get('k23', 0) # default None

# # создать 2 словаря разными способами:
# # 1. словарь с данными о польз (имя, юз, email)
# # 2. словарь с настройками профиля (тема, увед, язык)
# dict_user = {
#     'name': 'Andrysha',
#     'user_name': 'razriv_O4K',
#     'email': 'razriv_O4K@gmail.com'
# }

# settings = dict(zip(['theme','notification','language'],['dark','1','RU']))
# print (dict_user, settings, sep='\n')

# # crud 
# settings = {**settings, **{'font': 'Times'}}
# print(settings)
# settings['new_key'] = 'new_value'
# print(settings)

# del settings['new_key']
# print(settings)
# value = settings.pop('font3', 'key not found')
# print(value)

# settings['font'] = 'Arial'
# print(settings)

# print('theme' in settings)
# print('key' not in settings)

# print(list(settings.keys()))
# print(settings.values())
# print(settings.items())

# # генераторы
# dict_6 = {i:input() for i in [1, 2, 3]}
# print(dict_6)
# dict_7 = {i[0]:i[1] for i in [['eat','eat2'],['ea1','ea2']]}
# print(dict_7)

# Задача 1: на вход идет строка, необходимо составить словарь, где ключ - слово, а знач - кол-во
# повторов слова в строке
# вход: apple baNana Banana apple orange
# выход: {apple: 2, banana: 2, orange: 1}

'''
Задача 2: реализовать валидацию через словарь.
На вход идет значение возраста от 10 до 102 лет, все значение за границами этого диапазона
помечаются как "некорректные", валидные же данные помечаются как:
1. от 10 до 18 - "ребенок"
2. от 19 до 30 - "молодежь"
3. от 31 до 65 - "взрослый"
4. более 66 - "пенсионер"
При решение этой задачи нельзя использовать условный оператор и оператор switch case
'''
age = input()
try:
    age = int(age)
    if 10 <= age <= 102:
        # validator_1 = {
        #     "ребенок": list(range(10, 19)),
        #     # "молодежь": 19 <= age <= 30,
        #     # 31 <= age <= 65: "взрослый",
        #     # 66 <= age: "пенсионер"
        #     "молодежь": list(range(19, 31)),
        #     "взрослый": list(range(31, 66)),
        #     "пенсионер": list(range(66, 103))
        # }

        # for i in validator_1:
        #     if age in validator_1[i]:
        #         print(i)
        #         break
        # # print(validator)
        # validator_2 = {
        #     "ребенок": 10 <= age <= 18,
        #     "молодежь": 19 <= age <= 30,
        #     "взрослый": 31 <= age <= 65,
        #     "пенсионер": 66 <= age
        # }
        # # for i in validator_2:
        # #     if validator_2[i] == True:
        # #         print(i)
        
        # print(list(validator_2.keys())[list(validator_2.values()).index(True)])
        validator_3 = {
            10 <= age <= 18: "ребенок",
            19 <= age <= 30: "молодежь",
            31 <= age <= 65: "взрослый",
            66 <= age: "пенсионер"
        }
        print(validator_3[True])
    else:
        print("Некорректные данные")       
except:
    print("Некорректные данные")
'''
Задача 3: реализовать словарь синонимов.
На вход идет количество строк N, зачет перечисляются сами строки, в каждой строке записано по
2 слова через пробел. Пример:
3
hello Hi
list array
char symBol

Далее в терминал вводится одно любое слово из списка, в ответ выдается его синоним
Пример:
LISt -> Array
hi -> Hello
'''
# GoodBye Мы ушли хорошего дня 
# Дома доделать! Практику начать, на след паре буду спрашивать!
