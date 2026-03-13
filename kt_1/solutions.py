# task 1
age = input()

try:
    age = int(age)
    print('Полный доступ' if age >= 18 else ('Ограниченный доступ' if age >= 0 else 'Введите корректное значение'))
except:
    print('Введите корректное значение')

# task 2
score = 0
target = 30

while score < target:
    score  += 5
    print(f"Текущие баллы: {score}")

# if score >= 30:
print('Сертификат получен')

# task 3
# айдилист это пустой список массив фор нам ин рейнж ну я указываю четные числа 
id_list = list()
# id_list = []

for i in range(2, 21, 2):
    id_list.append(i)

print(id_list)

id_list_2 = [i for i in range(2, 21, 2)]
print(id_list_2)