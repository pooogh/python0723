# const x = 10;
# let y = 11;

x = 'Fedya'
print('Hello', x)

X = 10
print(X - 2, x)
print(type(10))
print(type(2.5))
print(type(True))
print(type('abc'))

# name = input()
# print('Hello,', name)
# age = int(input()) #'12'
# print(type(age))
# if age > 18:
#     print('adult')
# elif age == 18:
#     print('???')
# else:
#     print('child')
# print('exit')

# дано:
# k - студентов
# n - мандаринов
# сколько мандаринов достанется каждому студенту, а сколько останется?

# тернарный
# let x = y > 2 ? 'yes' : 'no';
y = 2
x = 1 if y > 2 else 3
print(x)

# циклы
while x < 10:
    print('x = ', x)
    x += 1
print('end')

for i in 'a', 2, True, 23:
    print(i)

test = [1, 2, 'asd', True, 5.8]
for i in test:
    print(i)

# (let i = 0, i < 10, i += 1)
for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -2):
    print(i)

# range(n) от 0 до n
# range(m, n) от m до n
# range(m, n, s) от m до n с шагом s

# на вход подается число n, найти n!
# 1. через while
# 2. через for
# n = 3 => 3! = 1 * 2 * 3

# генератор массива
zeros = [0, 1] * 10
print(zeros)

squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(squares)

n = 5
a = 1
d = -2
progr = [a + d * i for i in range(n)]
print(progr)
# :
#     progr.append()

'''
Даны целые числа N (> 2), A и B. 
Сформировать и вывести целочисленный массив размера N, первый элемент которого равен A, 
второй равен B, а каждый последующий элемент равен сумме всех предыдущих.
'''
[1, 2, 3, 6, 12, 24]
[2, 4, 6, 12, 24]
[3, 5, 8, 16, 32]

n = 10
a = 3
b = 7

arr = [a, b]
arr_tail = [arr.append(sum(arr)) for i in range(n)]

for i in range(n):
    arr.append(sum(arr))

# Условие
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# Условие
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import random
rand = [random.randint(0, 10) for i in range(10)]
print(rand)